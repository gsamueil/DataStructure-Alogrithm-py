"""
How to calculate power of a number using recursion ?
x^n = x*x*x*....(n times)...*x
x^n = x*x^(n-1)
"""
def power(base, exp):
    assert int(exp) == exp, 'the exponent must be integer number only'
    if exp == 0:
        return 1
    elif exp <0:
        return 1/base *  power(base, exp+1)

    return base * power(base, exp-1)

print(power(4, -1))