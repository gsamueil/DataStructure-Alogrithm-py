"""stack memory idea"""
#it will be print in method four first then three and two finaly will print in first function 
#and this is the idea for recursion

def first_method():
    second_method()
    print("i am the first method")

def second_method():
    third_method()
    print("i am the second method")

def third_method():
    fourth_method()
    print("i am the third methof")

def fourth_method():
    print("i am the fourth method")
#####################################
#another idea
def recursion_method(n):
    if n < 1:
        print (" n is less than 1")
    else:
        recursion_method(n-1)
        print(n)

if __name__ == '__main__':
    #first_method()
    recursion_method(4)

 