A=[]
N=int(input("Enter array size:"))

for i in range(N):
    c=int(input("Enter value:"))
    A.append(c)

def SelectionSort(A):
    n=len(A)
    for j in range(0,n-1):
        smallest=j
        for i in range(j+1):
            if(A[i]<A[smallest]):
                smallest=i
            A[j],A[smallest]=A[smallest],A[j]



print(A)
print("After selection sort")
SelectionSort(A)
print(A)

