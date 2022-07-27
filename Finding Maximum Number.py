def getKeyboardInput(A):
    for i in range (0,5):
        x=int(input("Enter a number:"))
        A[i] = x

def maxNumber(A):
    n=len(A)
    max=0
    for i in range(0,n):
        if(max<A[i]):
            max=A[i]
    return max

A=[0]*5
getKeyboardInput(A)
print (A)
y=maxNumber(A)
print(y)
