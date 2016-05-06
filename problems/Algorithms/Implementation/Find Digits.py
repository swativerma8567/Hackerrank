#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    sumEvenDivisible=0
    for i in str(n):
        if((int(i) > 0) and (int(n) % int(i) == 0)):
            sumEvenDivisible+=1
    print sumEvenDivisible       
    