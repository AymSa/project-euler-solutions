"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def sol_1():
    palindromes = []
    for x in range(100, 1001):
        for y in range(100, 1001):
            product = x*y
            if is_palindrome(product):
                palindromes.append(product)
    
    return sorted(palindromes)[-1]

if __name__ == '__main__':
    
    print(sol_1())
    pass 