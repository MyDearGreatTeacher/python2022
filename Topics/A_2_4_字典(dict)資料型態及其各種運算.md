# 字典(dict)資料型態及其各種運算
## 字典(dict)資料型態 Mapping Types — dict

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
a == b == c == d == e == f
```
- A mapping object maps hashable values to arbitrary objects. 
- Mappings are mutable objects. 
- There is currently only one standard mapping type, the dictionary. 
- A dictionary’s keys are almost arbitrary values. 
- Values that are not hashable, that is, values containing lists, dictionaries or other mutable types  may not be used as keys. 
- Numeric types used for keys obey the normal rules for numeric comparison: 
- if two numbers compare equal (such as 1 and 1.0) then they can be used interchangeably to index the same dictionary entry. 
- (Note however, that since computers store floating-point numbers as approximations it is usually unwise to use them as dictionary keys.)

## 字典(dict)資料型態的運算
- list(d)   Return a list of all the keys used in the dictionary d.
- len(d)   Return the number of items in the dictionary d.
- d[key]  Return the item of d with key key. Raises a KeyError if key is not in the map.
- d[key] = value  Set d[key] to value.
- del d[key]  Remove d[key] from d. Raises a KeyError if key is not in the map.
- key in d  Return True if d has a key key, else False.
- key not in d  Equivalent to not key in d.
- iter(d)  Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).
- clear()  Remove all items from the dictionary.
- copy()  Return a shallow copy of the dictionary.
- classmethod fromkeys(iterable[, value])   
  - Create a new dictionary with keys from iterable and values set to value.
  - fromkeys() is a class method that returns a new dictionary. 
  - value defaults to None. 
  - All of the values refer to just a single instance, so it generally doesn’t make sense for value to be a mutable object such as an empty list. 
  - To get distinct values, use a dict comprehension instead.
- get(key[, default]) 
  - Return the value for key if key is in the dictionary, else default. 
  - If default is not given, it defaults to None, so that this method never raises a KeyError.
- items()   Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
- keys()  Return a new view of the dictionary’s keys. See the documentation of view objects.
- pop(key[, default])
  - If key is in the dictionary, remove it and return its value, else return default. 
  - If default is not given and key is not in the dictionary, a KeyError is raised.
- popitem()  
  - Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.
  - popitem() is useful to destructively iterate over a dictionary, as often used in set algorithms. 
  - If the dictionary is empty, calling popitem() raises a KeyError.
  - Changed in version 3.7: LIFO order is now guaranteed. In prior versions, popitem() would return an arbitrary key/value pair.
- reversed(d)
  - Return a reverse iterator over the keys of the dictionary. This is a shortcut for reversed(d.keys()).
  - New in version 3.8.
- setdefault(key[, default])
  - If key is in the dictionary, return its value. 
  - If not, insert key with a value of default and return default. default defaults to None.
- update([other])
  - Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
  - update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). 
  - If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).
- values()  Return a new view of the dictionary’s values. 
