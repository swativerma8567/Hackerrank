#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    ontime=0
    for p in a:
       if(p)<=0:
        ontime+=1
    print("NO" if ontime>=k else "YES")   
        