# password generator
    # iterate
    # random number
    # rn => ascii character
    # cli

# random generator
import random

# function to reduce code
def randomPassword(passwordLen):

    # initialize password as empty string
    password = ""

    # iterate <passwordLen> times
    for x in range(passwordLen):

        #character = random int casted to ascii char
        character = chr(random.randint(32,126))

        # append character to password
        password += character

    # return completed password
    return password

# test function
# print(randomPassword(7))

