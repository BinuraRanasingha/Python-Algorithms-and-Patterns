def keyboardInput(A):
    i=0
    while(i<5):
        x=int(input("Enter a value:"))
        if(x>=10 and x<=20):
            A[i]=x
            i+=1

def insertsort(A):
    n=len(A)
    for j in range(1,n):
        key=A[j]
        i=j-1
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i=i-1
        A[i+1]=key
            



#--main--
A=[0]*5
keyboardInput(A)
print(A)
insertsort(A)
print(A)
