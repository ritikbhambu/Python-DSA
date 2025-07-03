def lastindex(arr, x):
    if len(arr) == 0:
        return -1
    
    # Recursively check the rest
    small = lastindex(arr[:-1], x)
    
    # If x is found at the last position of current arr
    if arr[-1] == x:
        return len(arr) - 1
    else:
        return small
 
print(lastindex([10,3,8,7,9,5],9))