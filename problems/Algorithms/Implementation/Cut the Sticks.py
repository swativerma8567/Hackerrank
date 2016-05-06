#!/bin/python

import sys

def mycond(arr):
    return arr-2 

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while len(arr)>0:
    print len([x for x  in arr if x-min(arr)>=0])
    arr= [x for x  in arr if x-min(arr)>0]

