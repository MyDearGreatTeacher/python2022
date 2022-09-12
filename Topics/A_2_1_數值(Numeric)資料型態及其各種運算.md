# 數值(Numeric)資料型態及其各種運算
- Numeric Types — int(整數), float(浮點數), complex(複數)
- There are three distinct numeric types: integers, floating point numbers, and complex numbers. 
- Booleans are a subtype of integers. 
- Integers have unlimited precision. 
- Floating point numbers are usually implemented using double in C
- information about the precision and internal representation of floating point numbers for the machine on which your program is running is available in sys.float_info. 
- Complex numbers have a real and imaginary part, which are each a floating point number. 
- To extract these parts from a complex number z, use z.real and z.imag. 
- (The standard library includes the additional numeric types fractions.Fraction, for rationals, and decimal.Decimal, for floating-point numbers with user-definable precision.)
- Numbers are created by numeric literals or as the result of built-in functions and operators. 
- Unadorned integer literals (including hex, octal and binary numbers) yield integers. 
- Numeric literals containing a decimal point or an exponent sign yield floating point numbers. 
- Appending 'j' or 'J' to a numeric literal yields an imaginary number (a complex number with a zero real part) which you can add to an integer or float to get a complex number with real and imaginary parts.
- Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the “narrower” type is widened to that of the other, where integer is narrower than floating point, which is narrower than complex. A comparison between numbers of different types behaves as though the exact values of those numbers were being compared. 2
- The constructors int(), float(), and complex() can be used to produce numbers of a specific type.

#
```python
import sys
sys.float_info
```
