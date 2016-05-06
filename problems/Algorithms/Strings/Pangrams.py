# Enter your code here. Read input from STDIN. Print output to STDOUT
def  findpangram(s):
    alphabets ="abcdefghijklmnopqrstuvwxyz"
    for x in alphabets:
        if(x not in s):
            #print "%s not in %s" %(x,s)
            return False
    return True
    

alphabets ="abcdefghijklmnopqrstuvwxyz"
s = str(raw_input().strip().lower())
s=s.replace(" ","")
#print s
if(findpangram(s)):
    print "pangram"
else:
    print "not pangram"

