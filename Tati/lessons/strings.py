#-----STRINGS-----#
# string is array of chars
a = "hello world"
print(a[1]) # e

# loop through string
for x in "banana":
    print(x)

# check string
txt = "this is a random sentence with words in it"
print("random" in txt)
if "random" in txt:
    print("yes, 'random' exists in txt")
print("nice" not in txt)

# slice
a = "Hello World"
print(a[2:5]) # llo; index 2 to 4
# from start
print(a[:5]) # Hello
# from end
print(a[2:]) # llo World
# negative index from end
print(a[-5:-2]) # orl

# modify string
print(a.lower()) # hello world
print(a.upper()) # HELLO WORLD
print("    Hello World") # Hello World
print(a.replace("H", "J")) # Jello World
print(a.split()) # ["Hello", "World"]

# concatenate
a = "Hello"
b = "World"
print(a + b) # HelloWorld
print(a + " " + b) # Hello World

# format
age = 21
print("My age is " + age) # error
print("My age is {}".format(age)) # My age is 21
itemNum = 12
price = 5
print("item num {0} is {1} dollars.".format(itemNum, price))

# escape chars
# \
txt = "this is my \"quote mark\"..."
### escape chars
# \' \" quotes
# \\ backslash
# \n newline
# \r carraige return; dont use
# \b backspace
# \f form feed; page break
# \ooo octal value
# \xhh hex value

# string methods
# https://www.w3schools.com/python/python_strings_methods.asp