# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

t=int(raw_input().strip())
for n in xrange(t):
    ran =raw_input().strip()
    min,max =(int(x) for x in ran.split())
    print int((math.floor(math.sqrt(max)) - math.ceil(math.sqrt(min))) + 1)