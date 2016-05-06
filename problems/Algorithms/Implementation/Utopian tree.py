#!/bin/python

import sys
import math


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    exp = int(round((float(n)/2))+1)
    if n==0:
        print 1
    elif n%2==0:
        print int(math.pow(2,exp)-1)
    else:
        print int(math.pow(2,exp)-2)
   
