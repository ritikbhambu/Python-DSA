def linear(arr,x,index):
    if index == len(arr):
        return False
    if arr[index]==x:
        return True
    small = linear(arr,x,index +1)
    if small:
        return True
    return False

print(linear([10,9,2,5,8,5,6],2,0))