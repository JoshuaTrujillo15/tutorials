# SEQUENTIALS

# list
# ordered, mutable, indexed
# duplicates allowed

thisList = ["apple", "banana", "cherry"]
print(len(thisList)) # 3

# can contain any data type, including mixed
thisMixedList = [1, "hello", True]

# access items
# index
print(thisList[1]) # "banana"

# negative index
print(thisList[-2]) # "apple"

# range of indexes
print(thisList[1:2]) # "banana", "cherry"
print(thisList[:2]) # "apple", "banana"
print(thisList[1:]) # "banana", "cherry"

# if exists
if "apple" in thisList:
    print("apple exists in list")

# change value of item
thisList[1] = "blackcurrant" # changes banana to blackcurrant

# append to list
thisList.append("orange") # adds orange to end

# insert at index
thisList.insert(1, "blueberry") # inserts blueberry to index 1
# apple, blueberry, blackcurrant, cherry, orange

# extend
thisOtherList = ["mango", "pineapple", "papaya"]
thisList.extend(thisOtherList)

# remove
thisList.remove("papaya")

# remove at index
thisList.pop(1) # removes at index 1
thisList.pop() # removes last item

del thisList[0] # removes at index 0
del thisList # delete list completely

# clear
thisList = [1,2,3]
thisList.clear() # []

# iter through list
thisList = ["apple", "banana", "cherry"]

for item in thisList:
    print(item)

# iter through index numbers
for iterator in range(len(thisList)):
    print("item name: {}, item number: {}".format(thisList[iterator], iterator))

# while loop
iterator = 0
while iterator < len(thisList):
    print(thisList[iterator])
    iterator += 1

# list comprehension
# uber shortcuts
[print(item) for item in thisList]

# example:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# create new list only with fruits containing the letter "a"

# without list comprehension
newList = []
for fruit in fruits:
    if "a" in fruit:
        newList.append(fruit)
print(newList)

newList = []

# with list comprehension
newList = [fruit for fruit in fruits if "a" in fruit]
print(newList)

# the syntax
# newList = [expression for item in list if condition == True]

# sorting alphanumerically
thisList.sort() # ascending
thisList.sort(reverse=True) # descending

# case insensitive sort
thisList.sort(key = str.lower)

# tuples
# ordered, immutable, indexed, allow duplicates

# sets
# immutable, unordered, unindexed, no duplicates, can add new items with .add()

# dictionaries
# unordered, no duplicates
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# access
model = thisDict["model"] # Mustang

# keys
keyList = thisDict.keys()

# items
itemList = thisDict.items() # returns list of keys and values in tuples

# add new item with key
thisDict["color"] = "white" # adds key "color" with value "white"

# change item
thisDict["color"] = "blue" # changes "white" to "blue"

