#!/bin/python

import sys

def getBlock(G,P,R,C,r,c):
    #print C-c+1
    #print R-r+1
    for x in xrange(R-r+1):
        for y in xrange(C-c+1):
            #print x,y
            if(matchSubArray(G,P,x,y,r,c)):
                return True
    return False        
            
            
def matchSubArray(G, P, x, y, r, c):
    #print "in matchSubArray"
    #print r,c
    for x1 in xrange(r):
        for y1 in xrange(c):
            #print "comparing G[%d + %d] [%d +%d] != P[%d] [%d]" % (x1,x,y1,y,x1,y1)
            #print "%s != %s" %(G[x+x1][y+y1],P[x1][y1])
            if(G[x+x1][y+y1]!= P[x1][y1]):
                
                #print "No Match Found"
                return False
    return True
      


t = int(raw_input().strip())
#t=1 # limit no of testcases for now (testing only)
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    #print "rows = %d , column = %d " %(R,C)
    G = []
    G_i = 0
    for G_i in xrange(R):
        #for wach row (goes from  0 to no of rows)
        G_t = str(raw_input().strip())
        G.append(G_t)  # G is your grid
    #print G    
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)
    #print P
    if (getBlock(G,P,R,C,r,c)):
        print "YES"
    else:
        print "NO"