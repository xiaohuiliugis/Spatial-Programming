# 10_9 unsolved
'''Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from the original. Hint: they don’t have to be in the same order.
'''
'''
def remove_duplicates(lis):
    s=lis[:]
    s.sort()

    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            del s[i]

    return s
'''
def remove_duplicates(lis):
    s=lis[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s.remove(s[i])
            
    return s

print remove_duplicates([1,3,5,7,4,2,3,5,9])

'''error occur when trying to deleting items from the list
'''
