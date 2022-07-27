#Recursive algorithm


x=0 #initializing variables
n=0

#function implementation
def power(x,n):
    if(n==0):
        return 1
    else:
        return x*power(x,n-1)

while(x!=-1):#loop executes until -1 is entered for x value
    x=int(input('Enter x(base):'))#taking keyboard input

    if(x==-1):#checking x value 
        break

    n=int(input('Enter n(exponent):'))

    print('The power=',power(x,n))
   
