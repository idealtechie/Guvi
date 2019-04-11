n=int(input())
a=input()
a=a.split()
k=[]
for i in a:
 if(a.count(i)==1):
  k.append(i)
print(k[0])
