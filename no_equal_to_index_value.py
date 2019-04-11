n=int(input())
a=input()
a=a.replace(" ","")
b=[]
for i in a:
 b.append(int(i))
k=[]
for i in range(0,len(b)):
 if(i==b[i]):
  k.append(i)
if(len(k)==0):
 print(-1)
else:
 print(*k)
