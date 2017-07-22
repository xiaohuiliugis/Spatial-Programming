# Exersie Chap 6_7

def is_power(a,b):
    if a%b==0:
        # use "if a> b " to make sure the recurse in the next line make sense
        if a> b and is_power(a/b,b)==True: 
            return True
        return True          
    else:
        return False

print is_power(2,4)
print is_power(4,2)
print is_power(25,5)
