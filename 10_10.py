# 10_10  

import time
"""Reads lines from a file and builds a list using append."""
def make_word_list1():
    t=[]
    fin=open('word.txt')
    for line in fin:
        word = line.split()
        t.append(word)
    return t
 
     
   
"""Reads lines from a file and builds a list using list +."""
def make_word_list2():
    t=[]
    fin=open('word.txt')
    for line in fin:
        word=line.split()
        t=t+[word]  # [word] is a great way of creating list
    return t

start_time= time.time()
t=make_word_list1()
elapse_time=time.time()-start_time

print len(t)
print t[:10]
print elapse_time,'seconds'

print len(t)
print t[:10]
print elapse_time, 'seconds'
