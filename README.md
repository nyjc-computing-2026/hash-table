# Hash Table Practice

The following function is provided:

`_hash_key(key)`
- takes in a `string` argument `key`
- returns a hashed `integer` value unique to the key.

The `_hash_key()` function implements the rolling polynomial algorithm as shown below:  
(Further reading: https://cp-algorithms.com/string/string-hashing.html)  
        
$hash(key) = (\sum_{i=0}^{n-1} key[i].p^i)\ mod\ m$

$ = (key[0] + key[1].p + key[2].p^2 + ... + key[n-1].p^{n-1})\ mod\ m$  
where
- `key` - each key segment is a string. It needs to be converted to its integer ASCII value 
- `p` - a small prime number (if the input is composed of only lowercase letters of the English alphabet,  
  $p = 31$  is a good choice. If the input may contain both uppercase and lowercase letters, then  
  $p = 53$  is a possible choice.)
- `m` - a large prime number (we will use $`10^9+9`$ for this implementation)

## Part 1: Hash table without collision resolution

In `hashtable.py`, implement the `HashTable` class:
- `__init__.py` should take a `size` parameter that determines the number of slots that the hashtable is initialised with.
- the fixed-size array that holds key-value pairs is represented as a Python `list`, pre-filled with `None` values
- do not use `list`-mutating methods and operators, such as `list.append()`, `list.extend()`, and list concatenation

and the following methods:
- `delitem(key)`
    - removes the key and its associated value from the hash table
    - raises a `KeyError` if the key is not found in the hashtable
- `getitem(key)` - returns the following:
    - returns the value associated with the key in the hash table
    - raises a `KeyError` if the key is not found in the hashtable
- `setitem(key, value)`
    - stores the key and value in the hash table
    - if the key exists in the hash table, its value is overwritten
