# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = map(int,raw_input().split())
#print n,k
problemsInChpList = [int(x) for x in raw_input().split()]
#print problemsInChpList
#problemsInChpList=[4,2,10]
totalPages=0
problemSet=[]
noOfSets=0
for x in problemsInChpList:
    #print "for %d problems" %(x)
    remProb=x
    startProb=1
    while(remProb > 0):
        if(remProb - k > 0):
            endProb = (startProb+k)
            problemSet=range(startProb,endProb)
            startProb=endProb
            remProb=remProb-k
        else:
            problemSet=range(startProb,(remProb)+startProb)
            remProb=0
               
        totalPages+=1
        #print "page %d = "%(totalPages)
        #print problemSet
        if (totalPages) in problemSet:
            noOfSets+=1
print noOfSets    
            
        
        
        
    