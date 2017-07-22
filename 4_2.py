def do_n(n):
    if n ==0:
        return
    print 'This is the '+ str(n) +'th recursion'
    do_n(n-1)

do_n(10)
