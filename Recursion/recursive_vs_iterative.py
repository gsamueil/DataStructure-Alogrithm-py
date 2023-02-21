def powerOfTwo(n):
    if n == 0:
        return 1

    else:
        power = powerOfTwo(n-1)
        return power * 2


def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n :
        power = power * 2
        i = i +1
    return power

if __name__ == '__main__':
    print(powerOfTwo(5))
    print(powerOfTwoIt(5))
