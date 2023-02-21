
"""
How to find the sum of digits of a positive integer number using recursion?
f(n) = n%10 + f(n//10)

10 10/10 = 1 and remainder = 0
54  54/10 = 5 and reainder = 4
112 112/10 = and remainder = 2
     11/10 = 1 and remainder = 1
"""
def sumofDigits(n):
    assert n>=0 and int(n) == n , 'the number has to be a positive integer only'
    if n == 0 :
        return 0
    else:
        return int(n%10) + sumofDigits(int(n//10))

print(sumofDigits(-15))