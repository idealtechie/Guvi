n=int(input())
k=[]
a=input()
a=a.split()
for i in set(a):
 if(a.count(i)>1):
  k.append(int(i))
if(len(k)>=1):
 m=sorted(k)
 print(*m)
else:
 print("unique")
 
