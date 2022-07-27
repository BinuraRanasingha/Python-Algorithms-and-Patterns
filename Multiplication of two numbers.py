M=0 #initialzing the variables to 0
n=0


#begining of function implementation
def Multiply(M,n):

    if(n==1):
        return M
    else:
        a=M+Multiply(M,n-1)#calling the Multiply function here
        return a

while(M!=-1 or n!=-1):#checking whether the value of M or n is -1
    M=int(input('Enter the first number:'))#getting keyboard inputs from

    if(M==-1): #checking whether M value is -1
        break
    
    n=int(input("Enter the second number:"))

    print("Multiplied Value=",Multiply(M,n)) #printing the final multiplied value
