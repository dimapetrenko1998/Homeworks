def test(*args):
    for arg in args:
        print(arg)


test(1, 'строка', True, [1, 2, 3])


def factorial(a=1):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)


result = factorial(5)
print(result)
