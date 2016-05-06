#!/bin/python
def insertionSort(ar):
    for index in xrange(1,len(ar)):
        currentEle=ar[index]
        position=index
        while(position>0 and ar[position-1]>currentEle):
            ar[position]=ar[position-1]
            position-=1
            print " ".join(str(p) for p in ar)
        ar[position]=currentEle
    print " ".join(str(p) for p in ar)
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
