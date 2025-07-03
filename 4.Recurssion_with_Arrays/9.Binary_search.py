def binary( arr,x,low,high):
    
    mid = (low+ high)//2
    if arr[mid]==x:
        return True
    elif arr[mid]<x:
        return binary(arr,x,mid+1,high)
    else:
        return binary(arr,x,low,mid-1)    
     


print(binary([10,20,30,40,50,60,70],60,0,6))