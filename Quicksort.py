n=int(input("Enter size of array:"));

def keyboardInput(A):
    i=0
    while(i<n):
        x=int(input("Enter a value:"))
        A[i]=x
        i+=1

def Partition(A,low,high):
    x=A[high]#pivot
    i=low-1#index of element
    for j in range(low,high):
        if(A[j] <= x):
            i=i+1#increment small element
            A[i],A[j] = A[j],A[i]

    A[i+1],A[high]=A[high],A[i+1]
    return (i+1)

def Quicksort(A,low,high):
    if(low<high):
        q=Partition(A,low,high)
        Quicksort(A,low,q-1)
        Quicksort(A,q+1,high)
            



#--main--
A=[0]*n
keyboardInput(A)
print(A)
Partition(A,0,n-1)
print("After partition",A)
Quicksort(A,0,n-1)
print("After quick sort",A)
