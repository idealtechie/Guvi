a=input()
k=[]
for i in a:
 if(i not in k):
  k.append(i)
print(*k,sep="")
