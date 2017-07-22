# Exercise 5

# 1st part

def print_gridrow():
    print '+','-'*4,'+','-'*4,'+','-'*4,'+','-'*4,'+'

def print_gridcol():
    print '|',' '*4,'|',' '*4,'|',' '*4,'|',' '*4,'|'

def do_four():
    print_gridcol()
    print_gridcol()
    print_gridcol()
    print_gridcol()

def do_mix():
    print_gridrow()
    do_four()

def do_mix2():
    do_mix()
    do_mix()
    print_gridrow()

do_mix2()
