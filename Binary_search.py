def Binary(arr,target):
    high = len(arr)-1
    low = 0
    while( low<=high):
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]> target:
            high =  mid-1
        elif arr[mid]< target:
            low = mid+1
        else:
            print("probably an error")        


arr = [10,20,30,40,50,60]
target = 60
print(Binary(arr,target))