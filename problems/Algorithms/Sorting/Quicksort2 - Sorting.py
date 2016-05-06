#!/bin/python
def quickSort(ar):    
    lenAr=len(ar)
    left=[]
    right=[]
    final=[]
    equal=[]
    if(lenAr <=1):
        return ar
    else:
        key=ar[0]
        for i in xrange(0,lenAr):
            if(ar[i] < key):
                left.append(ar[i])
            elif ar[i]== key:
                equal.append(ar[i])
            else:    
                right.append(ar[i])
  
        final =  quickSort(left) + equal + quickSort(right)
        print " ".join(map(str,final))
        return final
 
        
      

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
