

def _hash_key(key: str, p: int = 53) -> int:
    """Hashes the key using the rolling polynomial algorithm.

    Arguments:
    - key: str
      The key to be hashed.
    - p: int
      A prime number used for the rolling polynomial algorithm

    Returns:
    - the hashed location (int)
    """
    total = 0
    for i, char in enumerate(key):
        total += ord(char) * p**i
    return total


class HashTable:
    """A hashtable without collision resolution.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with

    Attributes:
    - size: int
      The number of slots that the hash table has
    - length: int
      The number of records contained in the hash table
    """

    def __init__(self, size: int):
        self.size = size
        self.length = 0
        self._data = [None] * size

    def __repr__(self) -> str:
        return f"HashTable(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        i = _hash_key(key)
        self._data[i] = value

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        i = _hash_key(key)
        value = self._data[i]
        if value is None:
            raise KeyError(f"'{key}' not found")
        return value

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        i = _hash_key(key)
        if self._data[i] is None:
            raise KeyError(f"'{key}' not found")
        self._data[i] = None


class HashTableLinearProbing(HashTable):
    """A hashtable that implements collision resolution using
    linear probing.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.

        Note: key and value are stored together as a (key, value) tuple
        """
        start = _hash_key(key)
        i = start
        # Probe until the starting point is reached again (with wraparound)
        while i + 1 != start:
            slot = self._data[i]
            # If slot is unoccupied, store (key, value) pair
            if slot is None:
                self._data[i] = (key, value)
                return
            stored_key, stored_value = slot  # slot is a (key, value) tuple
            # If matching key found, overwrite value
            if key == stored_key:
                self._data[i] = (key, value)
                return
            # Matching key not found; rehash key
            i = (i + 1) % self.size
        # If loop exits, no suitable slot found to store key-value pair;
        # Maybe hash table is full
        raise KeyError("Hash table is full")

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        start = _hash_key(key)
        i = start
        # Probe until the starting point is reached again (with wraparound)
        while i + 1 != start:
            slot = self._data[i]
            # If slot is unoccupied, key is not found
            if slot is None:
                raise KeyError(f"'{key}' not found")
            stored_key, stored_value = slot  # slot is a (key, value) tuple
            # If matching key found, return value
            if key == stored_key:
                return stored_value
            # Matching key not found; rehash key
            i = (i + 1) % self.size
        # If loop exits, key not found
        raise KeyError(f"'{key}' not found")

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        start = _hash_key(key)
        i = start
        # Probe until the starting point is reached again (with wraparound)
        while i + 1 != start:
            slot = self._data[i]
            # If slot is unoccupied, key is not found
            if slot is None:
                raise KeyError(f"'{key}' not found")
            stored_key, stored_value = slot  # slot is a (key, value) tuple
            # If matching key found, clear key-value
            if key == stored_key:
                self._data[i] = None
                # This will break subsequent probing; have to check
                # subsequent key-value pairs
                self._reinsert_probed_kvpairs(start=i)
                return
            # Matching key not found; rehash key
            i = (i + 1) % self.size
        # If loop exits, key not found
        raise KeyError(f"'{key}' not found")

    def _reinsert_probed_kvpairs(self, start: int) -> None:
        """Method invoked to reinsert probed key-value pairs

        Rationale:
        When a key-value pair is removed (and replaced with None),
        key-value pairs that relied on linear probing to be reached are
        no longer reachable.

        Solution:
        1. Inspect each key-value pair beginning from start
        2. Hash the key. If the key hashes to its current location, it
           does not rely on linear probing [can stop here]
        3. If the key does not hash to its current location, it relies
           on linear probing and needs to be re-inserted. [continue checking]
        4. If an empty slot is found, stop.
        """
        i = start
        while i + 1 != start:
            slot = self._data[i]
            if slot is None:  # (4)
                return
            key, value = slot  # (1)
            if _hash_key(key) == i:  # (2)
                return
            # (3) Reinsert key-value pair after removal
            self._data[i] = None
            self.setitem(key, value)
            # Continue checking
            i = (i + 1) % self.size


class HashTableSeparateChaining(HashTable):
    """A hashtable that implements collision resolution using
    separate chaining.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        raise NotImplementedError

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError
