# is a problem with the square sum
import math

''''
def checkInput(*t):
    inputlis = t[0]
    x=t[1]
    for s in inputlis:
        if isinstance(s,(int,long,float)) == True:
            findStats(t[0],x)
        else:
            return
'''        

def countLarge(inputList, largeNumber):

    total_1 = 0
    for value in inputList:
        if (value > largeNumber):
            total_1 = total_1 + 1

    return total_1

#finds the average value of a list (or tuple)
def findStats(*t):
    LargeNumbers = -1
    if (len(t) > 1):
        #find the number of values greater than X
        x = t[1]
        LargeNumbers = countLarge(t[0],x)

    inputList = t[0]
    total = 0
    for value in inputList:
        total = total + value
    mean = float(total) / float(len(inputList))

#This part calculates the St.DEV
    stDev =0
    squareSum = 0.0
    for value in inputList:
        squareSum += ((value-mean)**2)
    division = float(squareSum/float(len(inputList)-1))
    stDev = math.sqrt(division)
    

    if (LargeNumbers > -1):
        return total, mean, stDev,LargeNumbers
    else:
        return total, mean,
testList = [1,3,2]
print findStats(testList, 0)



