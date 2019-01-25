from factorize import factorize
from primes import primes_reduce, primes_filter, primes_comp


def test_factorize():
    assert factorize(99) == {11: 1, 3: 2}
    assert factorize(90) == {2: 1, 3: 2, 5: 1}


def test_primes():
    assert primes_reduce(20) == primes_filter(20) == primes_comp(20) == [2, 3, 5, 7, 11, 13, 17, 19]
