import sys
import math
import functools


# Borrowed implementation
def prod(nums):
    return functools.reduce(lambda a, b: a * b, nums, 1)

def chinese_remainder(remainders, divisors):
    M = prod(divisors)
    as_ = list(map(lambda d: int(M / d), divisors))
    eea_results = map(lambda tup: extended_gcd(*tup), zip(as_, divisors))
    is_ = [result[0] % div for result, div in zip(eea_results, divisors)]
    Z = sum(map(prod, zip(is_, remainders, as_)))
    x = Z % M
    return x

def extended_gcd(a, b):
    # EEA
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return Bezout coefficient 1, 2, and the gcd
    return old_s, old_t, old_r

if __name__ == "__main__":
    earlier_time = int(input())
    # To use Chinese remainder theorem, all elements here
    # must be coprimes.
    bus_times = input().split(',')

    rem = []
    div = []
    bus_tuples = []

    for i in range(0, len(bus_times)):
        if bus_times[i] == 'x':
            continue

        rem.append((-i) % int(bus_times[i]))
        div.append(int(bus_times[i]))
    print(rem)
    print(chinese_remainder(rem, div))