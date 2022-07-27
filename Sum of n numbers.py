n=0

def S(n):
    if(n==1):
        return 1
    else:
        return(S(n-1)+n)

while(n!=-1):
    n=int(input("Enter number:"))

    if(n==-1):
        break
    
    print("Sum=",S(n))
