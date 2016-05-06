# Enter your code here. Read input from STDIN. Print output to STDOUT


def compareList(sumArray,a,n):
    if(n == 1):
        return True
    sumFirstHalf = a[0]
    for z in xrange(1,n-1):
        sumSecondHalf = sumArray - sumFirstHalf - a[z]
        if(sumFirstHalf == sumSecondHalf):
            return True
        sumFirstHalf+=a[z]
    return False

if __name__ == "__main__":
    Tests = int(raw_input().strip())
    for x in xrange(0,Tests):
        n=int(raw_input().strip())
        a= [int(y) for y in raw_input().strip().split() ]
        sumArray = sum(a)
        if(compareList(sumArray,a,n)):
            print "YES"
        else:
            print "NO"
     
    
        