# Exercise 3

def is_between(x,y,z):
    if (x<=y and y<=z) == True:
        print 'ture'
        return True
    else:
        return False

x = raw_input('x')
y = raw_input('y')
z = raw_input('z')

is_between(int(x),int(y),int(z))
