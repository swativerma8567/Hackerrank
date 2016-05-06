#!/bin/python

import sys
import math

t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = (int(x) for x in raw_input().strip().split(' '))
    total=wrapper=n/c
    while wrapper >= m:
	   trade = wrapper / m
	   total += trade
	   wrapper = wrapper % m
	   wrapper = wrapper + trade
        
    print total    