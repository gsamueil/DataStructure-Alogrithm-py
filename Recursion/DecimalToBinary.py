"""How to convert number from decimal to binary using recursion"""
""""
division by       quotient        remainder
----------------------------------------------
13/2                6                  1
----------------------------------------------
6/2                 3                  0
----------------------------------------------
3/2                 1                  1
----------------------------------------------
1/2                 0                  1
-----------------------------------------------
13 = 1101

division by       quotient        remainder       1010
----------------------------------------------
10/2                5                  0
----------------------------------------------   101*10+0=1010
5/2                 2                  1       
----------------------------------------------   10*10+1 =101
2/2                 1                  0          
----------------------------------------------
1/2                 0                  1          1*10+0=10
-----------------------------------------------
10 = 1010

f(n) = n mod 2 + 10* f(n/2)
"""
def decimalToBinary(n):
    assert int(n) == n, 'the parameter must be an integer only'
    if n == 0:
        return 0
    else:
    

        return n%2 +10* decimalToBinary(int(n/2))
print(decimalToBinary(100))