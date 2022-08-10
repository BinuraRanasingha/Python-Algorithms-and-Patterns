instring = input('Enter string...')
num = ""

for i in range(len(instring)):
    if i % 2 == 0 :
        num = num + instring[i].lower()
       
       
    else:
         num = num + instring[i].upper()+'*'
  
    
print('The string is:',num)
