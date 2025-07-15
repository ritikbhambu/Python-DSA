def maxel(arr):
    if len(arr)==1:
        return arr[0]
    small=maxel(arr[1:])
    first = arr[0]
    if first > small:
        return first
    else:
        return small
print(maxel([1,2,3,4]) )   

 
