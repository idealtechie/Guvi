s="dhoni"
k=[]
for i in s:
    k.append(i)
a=input()
p=[]
for i in a:
    p.append(i)
if(len(k)==len(p)):
    for i in k:
        if (i not in p):
            flag="false"
            break
        else:
            flag="true"
else:
    flag="false"
    
if(flag=="false"):
    print("no")
else:
    print("yes")
