# SCOPE

# scope is where in the code heirarchy something exists

globalVariable = 1

def scopeStuffs():
    localVariable = 2
    return

for iterator in range(5):
    blockScopeVariable = iterator

# global scope
print(globalVariable) # 1

# local scope
scopeStuffs()
# print(localVariable) # error, does not exist
