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

a = float(input("Please intput num1: "))
b = float(input("Please intput num2: "))

print(f'''
{a} + {b} = {a+b}
{a} - {b} = {a-b}
{a} * {b} = {a*b}
gcd({a},{b}) = {gcd(a,b)}
''')