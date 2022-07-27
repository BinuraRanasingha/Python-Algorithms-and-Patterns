def Fibonacci(n):
    if(n<=1):
        return n
    else:
        return(Fibonacci(n-1)+Fibonacci(n-2))
    
n=int(input("Number of terms:"))

if n<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(Fibonacci(i))

