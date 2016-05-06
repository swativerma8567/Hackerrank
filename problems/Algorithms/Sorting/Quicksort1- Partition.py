#!/bin/python
def partition(ar):
    lenAr=len(ar)
    left=[]
    right=[]
    final=[]
    if(lenAr <=1):
        return ar
    else:
        key=ar[0]
        for i in xrange(0,lenAr):
            if(ar[i] < key):
                left.append(ar[i])
            else:
                right.append(ar[i])

        final=left+right
        print " ".join(map(str,final))
        
m = input()
ar=[]

ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
