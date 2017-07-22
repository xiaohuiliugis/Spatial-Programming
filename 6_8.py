# Exer 6_8

def gcd(a,b):
    r = a%b
    if r!=0:
        return gcd(b,r)
    else:
        return b 

print gcd(15,12)
'''
switch the two, if a<b, the remider = b, the recusion will execute gcd(b,a)
that automatically change the positions of the two
'''
print gcd(12,15)
print gcd(15,40)
