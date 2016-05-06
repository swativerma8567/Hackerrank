# Enter your code here. Read input from STDIN. Print output to STDOUT


def nextInc(n):
    i=len(n)-1
    while(i>0 and n[i-1]>=n[i]):
        i-=1
    if(i<=0):
        return False
      
    #find the sucessor for pivot(i-1) in right suffix    
    j=len(n)-1
    while(n[j] <= n[i-1]):
        j-=1
       
    #swap j and i-1
    n[j],n[i-1]=n[i-1],n[j]
    
    #sort suffix i and greater
    n[i:]=n[len(n)-1:i-1:-1]
    
    print "".join(map(str,n))
    return True
        
if __name__ == '__main__':
    m=input()
    for x in xrange(0,m):
        n=list(raw_input().strip())
        if not (nextInc(n)):
            print "no answer"