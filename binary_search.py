def BinarySearch(arr,x):
    low=0
    high=len(arr)-1
    mid=low+(high-low)//2
    if arr[mid]<x:
        low=mid+1
    elif arr[mid]>x:
        high=mid-1
    else:
        return mid
    return -1
arr=[10,20,30,40,50]
x=int(input("enter a number :"))
result=BinarySearch(arr,x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
            