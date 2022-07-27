A=[0]*8
def keyboardInput(A):
    i=0
    for i in range(0,8):
        x=int(input("Enter number:"))
        A[i]=x

keyboardInput(A)      
print(A)
    
def bubblesort(A):
    n=len(A)
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if(A[j]<A[j-1]):
                A[j],A[j-1]=A[j-1],A[j]


print(A)
print("After bubble sort")
bubblesort(A)
print(A)
