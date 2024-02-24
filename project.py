"""
just a simple calculater
"""
import time

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

def get_add(a: int, b: int) -> int:
    return a + b

def get_minus(a: int, b: int) -> int:
    return a - b

def get_muliple(a: int, b: int) -> int:
    return a * b

def get_two_integers():
    a = int(input("Please intput num1: "))
    b = int(input("Please intput num2: "))
    return a, b

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

def main():
    a, b = get_two_integers()
    calculate(a, b)

if __name__ == "__main__":
    main()
