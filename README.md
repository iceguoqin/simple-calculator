# simple-calculator
My final prject for CS50 Python course, a simple calculator.
### Video Demo: https://www.bilibili.com/video/BV1fC411W7yG/
### Description: 
A simple calculator, steps are here:
1. you input 2 numbers: a, b
2. calculate greates common devider of a and b
3. calculate a + b
4. calculate a - b
5. calculate a * b
### Project introduction
Well, wwe have only one file, project.py
It has 5 funtions that perform add operation, minus operation, multiple operation add get greatest common divider.
This is the add get_gcd() function:
```
def get_gcd(a: int, b: int) -> int:
    """
    get the greatest common devider of two numbers
    """
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)
```
### Refer: 
https://cs50.harvard.edu/python/2022/project/
