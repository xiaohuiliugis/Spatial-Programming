# Exercise 6_2
import math

def hypotenuse(leg_1,leg_2):
    squre1= (leg_1)**2
    squre2= (leg_2)**2
    sum = squre1+squre2
    result= math.sqrt(sum)
    print squre1,squre2,result
    return result

hypotenuse(3,6)
