n=int(input())
k=[]
a=input()
a=a.split()
for i in set(a):
 if(a.count(i)>1):
  k.append(int(i))
print(*k)
 
