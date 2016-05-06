#!/bin/python
def insertionSort(ar):
    #print " ".join(str(p) for  p in ar)
    counter=0
    for index in xrange(1,len(ar)):
        currEle=ar[index]
        position=index
        while(position >0 and ar[position-1]>currEle):
            ar[position]=ar[position-1]
            counter+=1
            position-=1
        ar[position]=currEle    
        #print " ".join(str(p) for  p in ar)    
    print counter

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)