"""Factorial"""
"""
-it is the product of all positive integers less than or equal to n.
-denoted by n! (christian kramp in 1808).
-only positive numbers.
-0!=1.
4! = 4*3*2*1 = 24
10! = 10*9*8*7*6*5*4*3*2*1 = 3628800
n! = n*(n-1)*(n-2)*.....*2*1.
if we neen more defination for how we calculate this term (n-1)*(n-2)*.....*2*1 it will be equal to (n-1)!
(n-1)! = (n-1)*(n-1-1)*(n-1-2)*.......*2*1 = (n-1)*(n-2)*.....*2*1
finally will be
n!= n*(n-1)!
fact(4)
   .
   .
   ......> 4*fact(3)
                  .
                  .
                  .........> 3* fact(2)
                                     .
                                     .
                                     ................> 2 * fact(1)

"""
#if we call function the stak memory will be infinity so we can import sys then used sys.setrecursionlimit
import sys
sys.setrecursionlimit
def factorial(n):
    assert n >= 0 and int(n) == n, 'the number must be positive integer only!'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5.1))