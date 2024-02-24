import project

def test_get_gcd():
    assert project.get_gcd(10, 25) == 5
    assert project.get_gcd(14, 28) == 14
    assert project.get_gcd(21, 56) == 7

def test_get_add():
    assert project.get_add(10, 5) == 15
    assert project.get_add(7, 10) == 17
    assert project.get_add(-3, 8) == 5

def test_get_minus():
    assert project.get_minus(10, 5) == 5
    assert project.get_minus(7, 10) == -3
    assert project.get_minus(-3, 8) == -11

def test_get_muliple():
    assert project.get_muliple(10, 5) == 50
    assert project.get_muliple(7, 10) == 70
    assert project.get_muliple(-3, 8) == -24

if __name__ == "__main__":
    test_get_gcd()
    test_get_add()
    test_get_minus()
    test_get_muliple()
