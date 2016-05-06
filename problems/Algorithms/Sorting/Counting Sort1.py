# Enter your code here. Read input from STDIN. Print output to STDOUT

n= int(raw_input().strip())
a=[0]*100


y = raw_input().strip().split()
for x in y:
    a[int(x)]+=1
print " ".join(map(str,a))   
    