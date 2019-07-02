a=input()
b=input()
b=b.split()
c=input()
c=c.split()
flag=1
for i in c:
    if(i not in b):
        flag=0
        break
if(flag==0):
    print("NO")
else:
    print("YES")
