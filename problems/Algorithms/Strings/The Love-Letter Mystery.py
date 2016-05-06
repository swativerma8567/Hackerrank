import math

n = int(raw_input().strip())

for x in xrange(n):
    y=str(raw_input().strip())
    leny=int(len(y))
    lenhalf = int(math.floor(leny/2))
    firsthalf = list(y[0:lenhalf])
    if leny %2 != 0:
        lenhalf = lenhalf+1
  
    secondhalf=list(y[lenhalf:leny])
    lensecondhalf=len(secondhalf)
    counter=0
    #print "len of second half = %d " %(lensecondhalf)
    b=lensecondhalf-1
    for a in xrange(lensecondhalf):
        #print "compare %s , %s" %(firsthalf[a],secondhalf[b])
        if(ord(firsthalf[a]) != ord(secondhalf[b])):
            counter+=int(math.fabs(ord(firsthalf[a]) -ord(secondhalf[b]) ))
        b-=1
    print counter
   
    

    