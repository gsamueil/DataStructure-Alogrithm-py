""""
How to find GCD (Greatest Common Divisor ) of  two numbers using recursion?
gcd(8,12) = 4
8 = 2*2*2
    - -
12 = 2*2*3
     - -
  Euclidean algorithm
gcd(a,0)=a
gcd(a,b)=gcd(b,a mod b)
gcd(48, 18)
48/18 = 2 renainder 12
18/12 = 1 remainder 6
12/6 =2 remainder 0

"""
def gcd(a, b):
      if b == 0 :
        return a
      else:

        return gcd(b, a%b)


print(gcd(48, 18))