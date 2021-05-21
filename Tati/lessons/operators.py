# OPERATORS

a = 5
b = 2
c = 5

# arithmetic
a + b # 7
a - b # 3
a * b # 10
a / b # 2.5
a % b # 1
a ** b # 25
a // b # 2

# assignment
d = 5
d += 3 # 8
d -= 3 # 5
d *= 3 # 15
d /= 3 # 5
d %= 3 # 2
# weird assignments not included, will describe after bitwise

# comparison
a == b # false
a != b # true
a > b # true
a < b # false
a >= b # true
a <= c # true

# logical
a > b and a == c # true
a == b or c > b # true
not(a == b) # true
#same as
a != b # also true

# identity
# same obj with same mem addr
x = []
y = []
z = x

x is y # false 
x is z # true
x is not y # true

# membership
# true if sequence is present in obj
y = [1, 2, 3]
2 in y # true
5 not in y # true

# bitwise
aBin = 0b0
bBin = 0b1
cBin = 0b1001

andResult = aBin & bBin # 0
orResult = aBin | bBin # 1
xorResult = aBin ^ bBin # 1
notResult = ~ bBin # 0
leftShiftResult = cBin << 2 # 0b0100
rightShiftResult = cBin >> 2 # 0b0010

# bitwise assignmment
cBin &= 3 # cBin = cBin & 3 aka cBin = 0b1001 & 0b0011
cBin |= 3 # 0b1011
cBin ^= 3 # 0b1010
cBin >>= 3 # 0b0001
cBin <<= 3 # 0b1000