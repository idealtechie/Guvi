a=input()
a=a.split()
b=[]
k=[]
x=0
y=0
for i in a:
    b.append(int(i))
p=sorted(b)
mi=p[len(p)-1]+p[len(p)-2]
for i in range(0,len(b)):
    for j in range(0,len(b)):
        if(i!=j):
            s=b[i]+b[j]
            if(s<mi and s>=0):
                x=b[i]
                y=b[j]
                mi=s
print(x,y)
    
