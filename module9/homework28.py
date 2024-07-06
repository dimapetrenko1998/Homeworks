def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


def min_func(int_list):
    return min(int_list)


def max_func(int_list):
    return max(int_list)


def len_func(int_list):
    return len(int_list)


def sum_func(int_list):
    return sum(int_list)


def sorted_func(int_list):
    return sorted(int_list)


print(apply_all_func([6, 20, 15, 9], max_func, min_func))
print(apply_all_func([6, 20, 15, 9], len_func, sum_func, sorted_func))
