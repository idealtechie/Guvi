a=input()
b=a.split()
c=set(b)
s=""
for i in range(0,len(c)):
 s=s+str(max(c))
 c.remove(max(c))
print(s)
