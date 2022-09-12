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
- 字典的每筆資料都使用key(鍵)=>value(值) pair(對)
- 每筆資料都使用冒號 : 分割
- 每對之間用逗號(,)分割，
- 整個字典包括在花括弧 {} 
- key(鍵)必須是唯一的，但value(值)則不必。
- Python 內建許多函數: len(dict):計算字典元素個數，即鍵的總數。
- Python 內建許多方法(Method):
  - 字典.items():以列表返回LIST陣列
  - 字典.keys():返回所有keys
  - 字典.values():返回所有values

## 字典(dict)資料型態的運算
- list(d)   ==>  Return a list of all the keys used in the dictionary d.
- len(d)    ==>  Return the number of items in the dictionary d.
- d[key]    ==>  Return the item of d with key key. Raises a KeyError if key is not in the map.
- d[key] = value  ==>  Set d[key] to value.
- del d[key]  ==>  Remove d[key] from d. Raises a KeyError if key is not in the map.
- key in d  ==>  Return True if d has a key key, else False.
- key not in d  ==>  Equivalent to not key in d.
- iter(d)  ==>  Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).
- clear()  ==>  Remove all items from the dictionary.
- copy()   ==>  Return a shallow copy of the dictionary.
- classmethod fromkeys(iterable[, value])   
  - Create a new dictionary with keys from iterable and values set to value.
  - fromkeys() is a class method that returns a new dictionary. 
  - value defaults to None. 
  - All of the values refer to just a single instance, so it generally doesn’t make sense for value to be a mutable object such as an empty list. 
  - To get distinct values, use a dict comprehension instead.
- get(key[, default]) 
  - Return the value for key if key is in the dictionary, else default. 
  - If default is not given, it defaults to None, so that this method never raises a KeyError.
- items()   ==>  Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
- keys()    ==>  Return a new view of the dictionary’s keys. See the documentation of view objects.
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
- values()  ==>  Return a new view of the dictionary’s values. 

## Dictionary view objects
- The objects returned by dict.keys(), dict.values() and dict.items() are view objects. 
- They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
- Dictionary views can be iterated over to yield their respective data, and support membership tests:
- 各種運算:
- len(dictview) Return the number of entries in the dictionary.
- iter(dictview) 
  - Return an iterator over the keys, values or items (represented as tuples of (key, value)) in the dictionary.
  - Keys and values are iterated over in insertion order. This allows the creation of (value, key) pairs using zip(): pairs = zip(d.values(), d.keys()). 
  - Another way to create the same list is pairs = [(v, k) for (k, v) in d.items()].
  - Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.
  - Changed in version 3.7: Dictionary order is guaranteed to be insertion order.
- x in dictview
  - Return True if x is in the underlying dictionary’s keys, values or items (in the latter case, x should be a (key, value) tuple).
- reversed(dictview)
  - Return a reverse iterator over the keys, values or items of the dictionary. 
  - The view will be iterated in reverse order of the insertion.
  - Changed in version 3.8: Dictionary views are now reversible.
- dictview.mapping
  - Return a types.MappingProxyType that wraps the original dictionary to which the view refers.
  - New in version 3.10.

# 範例學習
```python
dict = {'Name': 'DaDaLong', 'Age': 17, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict.items()
list(dict.items())
list(dict.keys())
```
### 使用字典(dict)資料寫成簡單的小寫英文字母 的[ASCII](https://en.wikipedia.org/wiki/ASCII)字典
  - a-->97  ... z-->122
- 範例1:key 是數字 value是小寫英文字母 97-->a  ... 122-->z
```python
ascii_a2z = {num: chr(num) for num in range(97,123)}
ascii_a2z
```
- 範例2:key 是小寫英文字母   value是 數字 a-->97  ... z-->122
```python
alphas= []
for num in range(97,123):
    alpha = chr(num)
    alphas.append(alpha)
 
ascii_a2z = {alpha: ord(alpha) for alpha in alphas}
ascii_a2z
``` 
