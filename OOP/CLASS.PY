class program:
    language = 'python'
    def Say_hello():
        print('hello world')

print(program.__dict__)    
my_func=program.__dict__['Say_hello']#the same idea
print(my_func())
print(getattr(program,'Say_hello')())#the same idea

