# 字串(string)資料型態及其各種運算:Text Sequence Type — str
# 字串(string)資料型態
- `Textual data(文字型資料)` in Python is handled with str objects, or strings. 
- Strings are immutable sequences of Unicode code points. 
- String literals are written in a variety of ways:
  - Single quotes: 'allows embedded "double" quotes'
  - Double quotes: "allows embedded 'single' quotes"
  - Triple quoted: '''Three single quotes''', """Three double quotes"""
    - Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

# String Methods字串(string)資料型態的各種運算
- str.capitalize()
- str.casefold()
- str.center(width[, fillchar])
- str.count(sub[, start[, end]])
- str.encode(encoding='utf-8', errors='strict')
- str.endswith(suffix[, start[, end]])
- str.expandtabs(tabsize=8)
- str.find(sub[, start[, end]])
- str.format(*args, **kwargs)
- str.format_map(mapping)
- str.index(sub[, start[, end]])
- str.isalnum()
- str.isalpha()
- str.isascii()
- str.isdecimal()
- str.isdigit()
- str.isidentifier()
- str.islower()
- str.isnumeric()
- str.isprintable()
- str.isspace()
- str.istitle()
- str.isupper()
- str.join(iterable)
- str.ljust(width[, fillchar])
- str.lower()
- str.lstrip([chars])
- str.maketrans(x[, y[, z]])
- str.partition(sep)
- str.removesuffix(suffix, /)
- str.replace(old, new[, count])
- str.rfind(sub[, start[, end]])
- str.rindex(sub[, start[, end]])
- str.rjust(width[, fillchar])
- str.rpartition(sep)
- str.rsplit(sep=None, maxsplit=- 1)
- str.rstrip([chars])
- str.split(sep=None, maxsplit=- 1)
- str.splitlines(keepends=False)
- str.startswith(prefix[, start[, end]])
- str.strip([chars])
- str.swapcase()
- str.title()
- str.translate(table)
- str.upper()
- str.zfill(width):Python zfill() 方法返回指定長度的字串，原字串右對齊，前面填充0

## 從網路上學習如何使用
### str.zfill(width):Python zfill() 方法返回指定長度的字串，原字串右對齊，前面填充0
- [Python String zfill() Method - Tutorialspoint](https://www.tutorialspoint.com/python/string_zfill.htm)
- [Python zfill()方法](https://www.runoob.com/python/att-string-zfill.html)
- [Python String zfill() Method - W3Schools](https://www.w3schools.com/python/ref_string_zfill.asp)
```python
#!/usr/bin/python

str = "this is string example....wow!!!";

print(str.zfill(40));
print(str.zfill(50));
```
