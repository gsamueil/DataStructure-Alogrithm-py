"""Fibonacci number"""
"""
Fibonacci sequence is a sequence of numbers in which each number is the sum of two preceding ones and
the sequence starts from zero and one.
0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
      .        .
      .        .
     0+1      3+5
 f(n) = f(n-1) + f(n-2)

"""
def fibonacci(n):
    assert n >=0 and int(n) == n , 'the number must be positive integer only!'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    