#10_6
'''
Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.

For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.
'''

def is_sorted(lis):
    
    for i in range(len(lis)-1):
        if lis[i] > lis[i+1]:
            return False
    return True 

        
print is_sorted([1,4,3])  #the result is true,bad solution

''' The following is a wrong one
it won't allow the loop to go through
all the elements in the list, and will return
as soon as any branch is right

def is_sorted(lis):
    bignumber=0
    for i in range(len(lis)-1):
        if lis[i] > lis[i+1]:
            return False
        if lis[i] < lis[i+1]:
            return True
