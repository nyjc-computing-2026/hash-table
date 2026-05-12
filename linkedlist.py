class Node:
    def __init__(self, key: str, value: dict):
        self.key = key
        self.value = value
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node(key={self.key!r}, value={self.value!r})"

    def set_value(self, value: dict) -> None:
        if not isinstance(value, dict):
            raise TypeError(f"value must be a dict")
        self.value = value


class LinkedList:
    def __init__(self):
        self._head: Node | None = None

    def get(self, key: str) -> dict:
        """Walks the linked list to search for a Node containing key.
        
        If found, returns the associated value.
        If not found, raises KeyError.
        """
        if self._head is None:
            raise KeyError("linked list is empty")
        node = self._head
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(f"'{key}' not found")

    def delete(self, key: str) -> None:
        """Walks the linked list to search for a Node containing key.
        
        If found, deletes (unlinks) the Node.
        If not found, raises KeyError.
        """
        if self._head is None:
            raise KeyError("linked list is empty")
        # If linkedlist head contains the key, unlink the head
        if self._head.key == key:
            self._head = self._head.next
            return
        prev = self._head
        node = self._head.next
        while node is not None:
            if node.key == key:
                # unlink node
                prev.next = node.next
                return
            prev = node
            node = node.next
        raise KeyError(f"'{key}' not found")

    def set(self, key: str, value: dict) -> None:
        """Walks the linked list to search for a Node containing key.
        
        If found, updates the value of the Node.
        If not found, raises KeyError.
        """
        if self._head is None:
            raise KeyError("linked list is empty")
        prev = None
        node = self._head
        while node is not None:
            if node.key == key:
                node.set_value(value)
                return
            prev = node
            node = node.next
        # If loop exits, no Node with key found
        # Add a new node at the end
        # Since node is None at this point, prev is the linkedlist tail
        prev.next = Node(key, value)
