alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
string=input()
flag=1
for i in alphabets:
 if (i not in string):
  flag=0
if(flag==0):
 print("no")
else:
 print("yes")
