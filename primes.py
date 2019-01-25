from functools import reduce


def primes_reduce(n):
    return list(reduce(lambda x, y: x if any(y % z == 0 for z in x) else x + [y], range(2, n + 1), []))


def primes_filter(n):
    return list(filter(lambda y: all(y % x != 0 for x in range(2, int(y ** 0.5) + 1)), range(2, n + 1)))


def primes_comp(n):
    return [x for x in range(2, n + 1) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]
