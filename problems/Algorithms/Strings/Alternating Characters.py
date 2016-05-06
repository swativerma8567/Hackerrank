# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
#print n
for x in xrange(n):
    s =str(raw_input().strip())
    l =len(s)
    #print "len = %d" %l
    s=list(s)
    counter=0
    for y in xrange(0,l-1):
        if (s[y] == s[y+1]):
            counter+=1
    print counter    
       