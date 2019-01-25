from factorize import factorize


def test_factorize():
    assert factorize(99) == {11: 1, 3: 2}
    assert factorize(90) == {2: 1, 3: 2, 5: 1}
