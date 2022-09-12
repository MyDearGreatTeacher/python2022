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
- 
