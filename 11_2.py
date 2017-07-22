# 11_2 

def histogram(s):
    d={'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
    for c in s:
        d[c]+= d.get('a',0)
        print d.get('a',0)
    return d
# The parameter for histogram should correspond to the key in d, otherwise
# will produce 'KeyError' (when a mapping (dictionary) key is not found in the set of existing keys)
histogram('abonsrut')
