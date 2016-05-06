
n= int(raw_input().strip())
a=[0]*100
l=[]

y = raw_input().strip().split()
for x in y:
    a[int(x)]+=1
    
for z in xrange(0,100):
    if a[z] >0:
        for p in xrange(0,a[z]):
            l.append(z)
print " ".join(map(str,l))   