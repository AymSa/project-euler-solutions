"""
Multiples of 3 or 5
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from math import floor

def sol_1(n):
    s = 0
    for i in range(n):
        if i%3 == 0 or i%5 ==0:
            s += i

    return s

def sol_2(n):
    return sum([i for i in range(n) if i%3 == 0 or i%5 == 0])

def sol_3(n):
    n_3 = floor((n-1) / 3)
    n_5 = floor((n-1) / 5)
    n_15 = floor((n-1) / 15)

    return 3*(n_3 * (n_3+1))/2 + 5*(n_5 * (n_5+1))/2 - 15*(n_15 * (n_15+1))/2


if __name__ == '__main__':
    n = 1000
    print(sol_1(n))
    print(sol_2(n))
    print(sol_3(n))