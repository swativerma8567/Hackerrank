# Enter your code here. Read input from STDIN. Print output to STDOUT

def findSol(a,amount,n):
    for z in xrange(0,n-1):
        for c in xrange(z+1,n):
                if((a[z] + a[c]) == amount):
                    print "%d %d"%(z+1,c+1)
                    return True
    return False
    

if __name__ == '__main__':
    test=int(raw_input().strip())
    for x in xrange(0,test):
        amount=int(raw_input().strip())
        n=int(raw_input().strip())
        a=[int(y) for y in raw_input().strip().split()]
        findSol(a,amount,n)
    