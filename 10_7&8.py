# 10_7
'''
Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.
'''
def is_anagram(t,s):
    nt =list(t)
    ns = list(s)
    nt.sort()
    ns.sort()
    if nt==ns:
        return True
    else:
        return False

print is_anagram('triangle','integral')
print is_anagram('triangle','igtegral')

# 10_8_1
'''Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
'''

def has_duplicates(lis):
    s=lis[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

# 10_8_2
'''If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.
'''

def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length (n)."""
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def count_match(n):
    count =0
    for i in range(samples):
        t=random_bdays(students)
        if has_duplicates(t):
            count +=1
    return count
        

        

    

