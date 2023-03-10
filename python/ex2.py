"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""
from math import sqrt

#Recursive mais pas du tout optimal pour résoudre ce problem 
def fibo_rec(n):
    if n > 1 :
        return fibo_rec(n-1) + fibo_rec(n-2)
    elif n == 1 :
        return 2
    else : 
        return 1 

def fibo(n): # Ici F0 = 0 et F1 = 1 
    phi = (1+sqrt(5))/2
    phi_prime = (1-sqrt(5))/2

    return (phi**n - phi_prime**n) / sqrt(5)

def sol_1(thresh):
    s = 0 
    a,b = 1,2
    while b < thresh:
        if b%2 == 0:
            s += b
        a,b = b, a+b
    return s  

if __name__ == '__main__':
    thresh = 4e6
    sol_1(thresh)