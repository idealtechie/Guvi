string=input()
string=string.replace(" ","")
a=[]
b=[]
for i in string:
 a.append(string.count(i))
maximum=max(a)
for i in string:
 if(string.count(i)==maximum):
  b.append(i)
print(b[0])
