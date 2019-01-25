from collections import defaultdict


def factorize(n):
    if n < 4:
        return [(n, 1)]
    ans = defaultdict(int)
    while n % 2 == 0:
        ans[2] += 1
        n /= 2
    divisor = 3
    while n > 1 and divisor <= int(n ** 0.5) + 1:
        while n % divisor == 0:
            ans[divisor] += 1
            n /= divisor
        divisor += 2
    if n > 1:
        ans[n] += 1
    return ans
