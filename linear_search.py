def linear(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1    

arr = [ 5,4,19,32,34,28]
target = 28
print(linear(arr,target))