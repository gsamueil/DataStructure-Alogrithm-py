"""A dictionary is a collection which is unordered , changeable and indexed"""
"""dictionary in memory  are indexed by keys and they can be seen as assoiative arrays."""
"""
python dictionaries are implemented using hash tables

"""
myDict = {"name": "George", "age": 39, "address": "Cairo"}
# TRAVERSE dictiomary
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])


# traverseDict(myDict)
# search in dict
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "Not exist"


print(searchDict(myDict, 39))
print(searchDict(myDict, 10))
# to remove item in dict we will used pop function
myDict.pop("name")
# if you need to see what you delete you must add print(myDict.pop("name"))
# to delete specific item we can used popitem
# if we need to delete all items we can used clear function
# also we can used del mydict['key name']
# del mydict   to delete every thing
print(myDict)
