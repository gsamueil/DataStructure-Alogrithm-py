class Solution(object):
    def rotate(self):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = int(input("enter number of row"))
        n = int(input("enter number of column"))
        a = []
        for i in range(m):
            b = []
            for j in range(n):
                j = int(input("enter number in pocket[" + str(i) + "][" + str(j) + "]"))
                b.append(j)
            a.append(b)
        print("Matrix is ....")
        for i in range(m):
            for j in range(n):
                a[i][j], end = " "
            print()
        return matrix

    def transpose_(self, a):
        self.rotate()
        b = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[j][i])
            b.append(c)
        for i in range(len(b)):
            for j in range(len(b[0]) - 1, -1, -1):
                print(b[i][j], end=" ")
            print()
        return a


ob = Solution()
matrix = ob.rotate()
ob.transpose_(matrix)
