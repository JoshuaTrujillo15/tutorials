# FUNCTIONS
    # repeatable blocks of code

def getAvg(firstNum, secondNum):
    avg = (firstNum + secondNum) / 2
    return avg

def main():
    x = 5
    y = 4
    xyAvg = getAvg(x, y)

    a = 3
    b = 35

    abAvg = getAvg(a, b)

    print("the avg of a and b is {}, and the avg of x and y is {}".format(abAvg, xyAvg))




main()