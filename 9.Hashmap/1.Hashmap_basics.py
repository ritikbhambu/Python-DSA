# ✅ Use immutable and hashable types as dictionary keys.

# Examples: int, str, tuple (with immutables), frozenset

# ❌ Avoid mutable types like list, dict, set as keys.

# Reason: Keys need a constant hash value — mutable objects can change, breaking that.




#  Creating a sample dictionary
hashmap = {'a': 1, 'b': 2}

# 1. get() – Safely retrieve value with optional default
print(hashmap.get('a'))       # Output: 1
print(hashmap.get('z', 'NA')) # Output: 'NA' (key doesn't exist)

# 2. setdefault() – Get value if key exists, else set it with default
hashmap.setdefault('c', 0)
print(hashmap)  # {'a': 1, 'b': 2, 'c': 0}

# 3. update() – Merge another dict into the current one
hashmap.update({'d': 4})
print(hashmap)  # {'a': 1, 'b': 2, 'c': 0, 'd': 4}

# 4. pop() – Remove a specific key and return its value
removed_value = hashmap.pop('b')
print(removed_value)  # Output: 2
print(hashmap)        # {'a': 1, 'c': 0, 'd': 4}

# 5. popitem() – Remove and return the last inserted key-value pair
last_item = hashmap.popitem()
print(last_item)  # Output: ('d', 4)
print(hashmap)    # {'a': 1, 'c': 0}

# 6. clear() – Remove all items from the dictionary
hashmap.clear()
print(hashmap)  # Output: {}

# Re-creating for further examples
hashmap = {'x': 10, 'y': 20, 'z': 30}

# 7. values() – Return all values
print(list(hashmap.values()))  # Output: [10, 20, 30]

# 8. keys() – Return all keys
print(list(hashmap.keys()))  # Output: ['x', 'y', 'z']

# 9. items() – Return all key-value pairs as tuples
print(list(hashmap.items()))  # Output: [('x', 10), ('y', 20), ('z', 30)]

# 10. copy() – Shallow copy of the dictionary
copy_dict = hashmap.copy()
print(copy_dict)  # Output: {'x': 10, 'y': 20, 'z': 30}

# 11. fromkeys() – Create a new dict from keys with a common value
keys = ['k1', 'k2', 'k3']
new_dict = dict.fromkeys(keys, 100)
print(new_dict)  # Output: {'k1': 100, 'k2': 100, 'k3': 100}

# 12. __contains__() or 'in' – Check if a key exists in the dictionary
print('x' in hashmap)  # Output: True
print('a' in hashmap)  # Output: False
