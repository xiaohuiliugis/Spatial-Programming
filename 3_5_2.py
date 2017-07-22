# Exercise 5
# 2nd part
def print_gridrow():
    print ' + - - - -'*4,'+'
def print_gridcol():
    print ' |        '*4,'|'

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
def do_mix4():
    do_mix2()
    do_mix2()

do_mix4()
print_gridrow()
