# Ex 6_6_1
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print middle('abc')

# Ex 6_6_2

def is_palidrome(string):
    if len(string)<=1:
        return True
    if first(string)!= last(string):
        return False
    return is_palidrome(middle(string))

print is_palidrome('x')
print is_palidrome('xx')
print is_palidrome('xhx')
print is_palidrome('fastsaf')
print is_palidrome('style')
print is_palidrome('graduate')



