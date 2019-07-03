a=input()
a=a.split()
n=int(a[1])
b=input()
b=b.split()
c=[]
for i in b:
 c.append(int(i))
d=sorted(set(c))
ans=d[len(d)-n]
print(ans)
