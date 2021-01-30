#initial test
print("Hello World!")

#-----BASICS-----#

# comments work like this
'''
this is a hack for
multi line
comments
'''
# quotes
# '' or ""

# info about python
'''
python
    interpreted, NOT compiled
    high level
    slower than low level
        high level: fast to develop, slow to run
        low level: slow to develop, fast to run
    reduces overhead

data
    binary, 0b, 0B,
    hex, 0x lower, 0X upper, 4 bits
    byte, b, B, 8 bits
    various datatypes
'''


#-----SYNTAX----#

# imports
import random as rng

# indention must be consistent
if (5<4):
    print("dang")

# variable created when value assigned
x = 5

#naming conventions
'''
snake_case
MACRO_CASE
camelCase
CapWords
'''

# data types
'''
text
    str
        string of chars

numeric
    int
        pos or neg, no decimal, infinite length
    float
        pos or neg, decimal
    complex
        numj, j is imaginary part

sequential
    list
        [] variable size, more useful than tuple, ordered, indexed
    tuple
        () fixed size, ordered, indexed
    set
        {} unordered, unindexed
    range
        function that starts at 0, increments by 1 until end
            range(end)

mapping
    dict
        {} no index, uses keys

boolean
    bool
        true or false
        truthy
            non empty string
            non 0 number
            non empty list, tuple, dictionary
        falsey
            empty string, dictionary, list, tuple
            0
            None

binary
    bytes
        immutable obj
    bytearray
        mutable array of bytes
    memoryview
        shows where in memory, addr in hex, 0x

'''

# random numbers

print(rng.randrange(1,10))

# casting

x = 1
a = str(1)
b = float(a)
c = int(b)
print(c)