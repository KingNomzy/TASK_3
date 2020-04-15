
import re
x = True
pword = input("Enter your password ")
while x:
    if (len(pword)<6 or len(pword)>12):
         break
    elif not re.search ("[A-Z]", pword):
         break
    elif not re.search ("[a-z]", pword): 
         break
    elif not re.search ("[0-9]", pword):
         break
    else:
        print("Password correct")
        x = False
        break
if x:
    print("Incorrect password")
