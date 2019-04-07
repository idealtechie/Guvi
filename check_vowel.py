a=input()
a=a.lower()
vowel=['a','e','i','o','u']
if (a.islower() and len(a)==1):
 if(a in vowel):
  print("Vowel")
 else:
  print("Consonant")
else:
 print("invalid")
 
