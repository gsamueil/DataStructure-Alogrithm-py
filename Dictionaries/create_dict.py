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


traverseDict(myDict)
# s
