base=0 #initializing variables to zero
exp=0

#function implementation begins here
def Power(base,exp):
    if(exp==0):#checking whether exp=0
        return 1
    else:
        return base*Power(base,exp-1)

while(base != -1):#loop continues until base=-1
    base=int(input("Enter the base value:"))#prompting user input

    if(base==-1):#checking whether base=-1
        break

    exp=int(input("Enter the exponenet value:"))

    print("Power=",Power(base,exp))#printing power value
    
    
    
