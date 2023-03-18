def middle(lst):
    new = lst[1:]
    del new[-1]
    return new


list = [1, 2, 3, 4, 6, 7]
print(middle(list))


def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    return sum


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sumDiagonal(myList2D))  # 15


def firstSecond(given_list):

    a = given_list  # make a copy

    a.sort(reverse=True)

    print(a)

    first = a[0]

    second = None

    for element in given_list:

        if element != first:

            second = element

            return first, second


def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)


def pairSum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) + "+" + str(myList[j]))
    return result
