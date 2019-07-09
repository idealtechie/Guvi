from itertools import permutations
z=input()
k=permutations(z)
r=[]
for i in list(k):
    s="".join(list(i))
    if(s not in r):
        r.append(s)
for i in r:
    print(i)
