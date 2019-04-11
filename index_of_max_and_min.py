n=int(input())
a=input()
a=a.split()
k=[]

for i in a:
    k.append(int(i))
x=max(k)
y=min(k)
for i in range(0,len(k)):
    if(k[i]==x):
        mx=i+1
    if(k[i]==y):
        mn=i+1
print(str(mn)+" "+str(mx))
