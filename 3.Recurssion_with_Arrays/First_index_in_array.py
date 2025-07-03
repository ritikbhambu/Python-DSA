def firstindex(arr,x):
    if len(arr)==0:
        return -1
    if  arr[0]==x:
        return 0
    small = firstindex(arr[1:],x)
    if small ==-1:
        return small
    else:
        return small+1
    
print(firstindex([10,5,2,9,7,4],9))    