# 列表(list)資料型態及其各種運算
- [Python Lists - W3Schools](https://www.w3schools.com/python/python_lists.asp)
- [Python 列表(List)]()
- [Python List (With Examples) - Programiz]()
# 列表(list)資料型態
- 列表(list)資料型態 ==> `mylist = ["apple", 2022, 65536.168, "iphone 14 Pro Max", "MAC", 2022]`
- Lists are created using `square brackets`
- Lists are used to store multiple items(List Items) in a single variable.
  - a list of `comma-separated values (items)` between `square brackets`
  - A list can have any number of items and they may be of different types (integer, float, string, etc.)
  - List items are ordered, changeable, and allow duplicate values.
  - List items are indexed, the first item has index [0], the second item has index [1] etc.
  - Allow Duplicates: Since lists are indexed, lists can have items with the same value:
- list是一個`類別(class)` ==> `list()` constructor 加上一堆方法

# 列表(list)資料型態的基本運算
- Access List Elements:Accessing Values in Lists
- Negative indexing
- Slicing of a List
- Negative index List slicing
- List Comprehension:
  - used for creating new lists from other iterables like tuples, strings, arrays, lists, etc. 
  - A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.  

# 列表(list)資料型態的各種運算
- 使用Python的函數:
  - cmp(list1, list2):比較兩個列表的元素
  - len(list):回傳列表元素的個數
  - max(list):回傳列表元素最大值
  - min(list):回傳列表元素最小值
  - list(seq):將`元組(seq)`轉換為`列表(list)` ==>`list()` constructor

- 使用Python list類別的方法(method)
  - list.append(obj):在列表末尾添加新的obj物件
  - list.count(obj):統計某個obj在列表中出現的次數
  - list.extend(seq):在列表末尾一次性追加另一個序列中的多個值（用新列表擴展原來的列表）
  - list.index(obj):從列表中找出某個值第一個匹配項的索引位置
  - list.insert(index, obj):將obj插入列表
  - list.pop([index=-1]):移除列表中的一個元素（預設最後一個元素），並且返回該元素的值
  - list.remove(obj):移除列表中某個值的第一個匹配項
  - list.reverse():反向列表中元素
  - list.sort(cmp=None, key=None, reverse=False):對原列表進行排序


# 範例學習:請自行擴充各種範例
### 列表(list)資料型態的基本運算
```python
mylist = ["apple", 2022, 65536.168, "iphone 14 Pro Max", "MAC", 2022]

# Access List Elements:Accessing Values in Lists
mylist[0]
mylist[4]

# Negative indexing
mylist[-3]
mylist[-1]

# 各種切片(Slicing)技巧 Slicing of a List
mylist[:3]
mylist[2:]
mylist[:]

# Negative index List slicing
mylist[ : : -1]
```
### List Comprehension
```
X_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(X_square)

X2_square = [x ** 2 for x in range(1, 11) if x % 2 != 1]
print(X2_square)
```

- 更多範例學習
  - [Python program to interchange first and last elements in a list](https://www.geeksforgeeks.org/python-swap-elements-in-string-list/)
  - [Python List Comprehension and Slicing](https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/)
  - [Nested List Comprehensions in Python](https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/)
  - [Python – Swap elements in String list](https://www.geeksforgeeks.org/python-swap-elements-in-string-list/)

## 列表(list)資料型態的各種運算
