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
It has some funtions that perform add operation, minus operation, multiple operation add get greatest common divider.
This is the get_gcd() function:
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
This is the add() function:
```
def get_add(a: int, b: int) -> int:
    return a + b
```
This is the minus function:
```
def get_minus(a: int, b: int) -> int:
    return a - b
```
This is the multiple function:
```
def get_muliple(a: int, b: int) -> int:
    return a * b
```
This is the funtion that you get inputs:
```
def get_two_integers():
    a = int(input("Please intput num1: "))
    b = int(input("Please intput num2: "))
    return a, b
```
This is the function that performs calculate logic:
```
def calculate(a: int, b: int):
    gcd_num = get_gcd(a, b)
    add_num = get_add(a, b)
    minus_num = get_minus(a, b)
    muliple_num = get_muliple(a, b)
    time.sleep(1)
    print(f'a + b       == {add_num}')
    print(f'a - b       == {minus_num}')
    print(f'a * b       == {muliple_num}')
    print(f'gcd(a, b)   == {gcd_num}')
```
Finally is the main function:
```
def main():
    a, b = get_two_integers()
    calculate(a, b)
```
Another file is test_project.py, here is an example:
```
def test_get_add():
    assert project.get_add(10, 5) == 15
    assert project.get_add(7, 10) == 17
    assert project.get_add(-3, 8) == 5
```

### Refer: 
https://cs50.harvard.edu/python/2022/project/
