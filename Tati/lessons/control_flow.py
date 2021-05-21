# if / else statements
a = 33
b = 255
c = 24

if a < b:
    print("a is smaller than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

# and
if a < b and a > c:
    print("both conditions are true")

# or
if a < b or a > c:
    print("at least one of the conditions is true")

# nested if
if a > 10:
    print("a is greater than 10,")
    if a > 20:
        print("and 20")
    else:
        print("but less than 20")

# pass
# if cannot be empty, use pass 
if b > a:
    pass

# while
i = 1
while i < 6:
    print(i)
    i += 1

# for
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# for through string
for i in "banana":
    print(i)

# range
for i in range(3):
    print(i)

# for else
for i in range(3):
    print(i)
else: 
    print("loop complete")

# nested loop
adjectives = ["apple", "banana", "cherry"]
for x in adjectives:
    for y in fruits:
        print(x, y)

# pass
for x in range(3):
    pass

# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# while else
i = 1
while i < 6:
    print(i)
    i += 1
else: 
    print("i is no longer less than 6")

# short hand:
    # if
    if a > b: print("a is greater than b")

    # if else
    print("a") if a > b else print("b")