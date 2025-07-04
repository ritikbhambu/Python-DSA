def quick(arr,low,high):
    if low>high:
        return
    pivot = part(arr,low,high)
    quick(arr,low,pivot-1)
    quick(arr,pivot+1,high)

def part(arr,low,high):
     
    idx = low -1 # for multiple calls it is possible that i is non zero so assign idx just before its value
    i = 0
    for i in range(low,high):
        if arr[i]<arr[high]:
            idx+=1
            arr[idx],arr[i] = arr[i],arr[idx]
    arr[idx+1],arr[high] = arr[high],arr[idx+1]
    return idx+1            



arr = [19,3,9,12,4,19]
quick(arr,0,len(arr)-1)
print(arr)