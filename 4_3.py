# Exercise 3_1
import math

def check_fermat(a,b,c,n):
    
    if n>=2 and math.pow(a,n)+ math.pow(b,n)== math.pow(c,n):
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that doesn’t work'

# Exercise 3_2

a = raw_input('Please enter a vaue for a:')
b = raw_input('Please enter a vaue for b:')
c = raw_input('Please enter a vaue for c:')
n = raw_input('Please enter a vaue for n:')

check_fermat(int(a),int(b),int(c),int(n))



         
            
        
        

