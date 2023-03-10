"""
What is the largest prime factor of the number 600851475143
"""
from math import sqrt, ceil


def is_prime(n):
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False
    return True


def sol_1(n):
    for i in reversed(range(2, ceil(sqrt(n)))):
        if n % i == 0 and is_prime(i):
            return i
    return n

if __name__ == "__main__":
    n = 2
    print(sol_1(n))
