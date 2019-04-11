a=input()
a=a.split()
s=[]
for i in a:
 s.append(i[::-1])
for i in range(0,len(s)-1):
 print(s[i],end=' ')
print(s[len(s)-1])
