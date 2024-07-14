def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if is_prime_number(result):
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
