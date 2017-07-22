# Lab Assignment_ Exercise 2
import math

def distance(x1,y1,x2,y2):
    dx = float(x2)-float(x1)
    dy = float(y2)-float(y1)
    dsquared = dx**2+ dy**2
    return math.sqrt(dsquared)


x1=raw_input('Please enter the x coordinate of the 1st vertex: ')
y1=raw_input('Please enter the y coordinate of the 1st vertex: ')
x2=raw_input('Please enter the x coordinate of the 2nd vertex: ')
y2=raw_input('Please enter the y coordinate of the 2nd vertex: ')
    

while True:
    reply = raw_input('Is the polyline complete? Yes or No ?')
'''
d needs to be placed inside while loop, because it will only be used
inside while loop. And otherwise the loop will never ends
'''
    d = distance(x1,y1,x2,y2)
    if reply.upper() == 'YES':
        print 'The length of the polyline is:', d
        break
        
    elif reply.upper() == 'NO':
        x=raw_input('Please enter the x coordinate of the vertex: ')
        y=raw_input('Please enter the y coordinate of the vertex: ')
        d=d+distance(x1,y1,x,y)
            

        

        
        
