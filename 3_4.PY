# Exercise 3-2

def do_twice(f,value):
    f(value)
    f(value)

# Exercise 3-3

def print_twice(str):
    print str
    print str

# Exercise 3-4

# do_twice(print_twice,'spam')

# Exercise 3-5

def do_eight(f,value):
    do_twice(f,value)
    do_twice(f,value)

do_eight(print_twice,'spam')


