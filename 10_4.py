#10_4
def middle(lis):
    lis.pop(0)
    lis.pop(-1)
    return lis

print middle([1,2,3,4,5])

#10_5
def chop(lis):
    del lis[0]
    del lis[-1]

