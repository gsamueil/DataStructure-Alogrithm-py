""" tuples is asequence of values much like a list . the value stored in tuple  can be any type and they are indexed by integers ."""
newTuple = ("a", "b", "c", "d", "e")
print(newTuple[1])
print(newTuple[:])
print(newTuple[1:3])
init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)

print(result)
