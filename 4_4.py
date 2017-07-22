# Exercise 4_1

def is_triangle(a,b,c):
    if (a+b)>= c or (a+c)>=b or (b+c)>=a:
        print 'Yes'
    else:
        print 'No'

# Exercise 4_2

a = raw_input('Please enter 1st stick length:')
b = raw_input('Please enter 2nd stick length:')
c = raw_input('Please enter 3rd stick length:')

is_triangle(int(a),int(b),int(c))

