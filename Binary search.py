A=[]
print("Enter sorted array:")

for i in range(0,5):
    x=int(input(""))
    A.append(x)

def BinarySearch(A,min,max,key):
    if (max<min):
        return false
    else:
        mid=((min+max)//2)
        if A[mid]>key:
            return BinarySearch(A,min,mid-1,key)
        elif A[mid]<key:
            return BinarySearch(A,mid+1,max,key)
        else:
            return mid

c=BinarySearch(A,0,len(A)-1,20)
print("Key is available at the index:",c)
