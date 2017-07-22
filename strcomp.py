def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        i = 0
        j = len(word2)

        while j > 0:
            if word1[i] != word2[j-1]:
                return False
            i = i+1
            j = j-1

        return True
        
    
if is_reverse('look','kohl'):
    print 'yes'
else:
    print 'no'
