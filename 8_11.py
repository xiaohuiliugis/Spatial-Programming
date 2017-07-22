# 8_11  Do no understand

import string

def rotate_letter(letter,n):
    # rotate a letter by n places. Does not change other chars

    # letter: single-letter string
    # n: int

    # returns: single-letter string

    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start= ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c+n)%26 + start
    
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print rotate_word('cheer', 7)
    print rotate_word('melon', -10)
    print rotate_word('sleep', 9)
