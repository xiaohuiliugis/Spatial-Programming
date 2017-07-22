#A step size of 2 means every other character; 3 means every third, etc.
# A step size of -1 goes through the word backwards,
# so the slice [::-1] generates a reversed string.

def is_panlindrome(word):
    if word[: : -1]==word:
        return True

print is_panlindrome('lpoopl')
