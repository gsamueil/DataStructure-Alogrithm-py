"""list of strings"""

# a = 'spam and notspam'
# b = list(a)
a = 'spam-and-notspam'
delimiter = '-'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))
