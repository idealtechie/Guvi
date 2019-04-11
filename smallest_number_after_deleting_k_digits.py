a=input()
b=a.split()
z=b[0]
d=int(b[1])
num=[]
k=[]
s=""
for i in z:
 num.append(int(i))
for i in range(d,len(num)):
 k.append(num[i])
for i in range(1,len(k)+1):
 s=s+str(min(k))
 k.remove(min(k))
print(s)
