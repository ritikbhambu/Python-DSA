def merge(arr,low,high):
    if(low<high):
        mid = (low + high)//2
        merge(arr,low,mid)
        merge(arr,mid+1,high)
        submerge(arr,low,mid,high)
def submerge(arr,low,mid,high):
    i = low
    j = mid+1
    b = [0]*(high-low+1)
    k = 0
    while i<=mid and j<=high:
        if arr[i]<arr[j]:
            b[k] = arr[i]
            i+=1
            k+=1
        else:
            b[k] = arr[j]
            j+=1
            k+=1
    while i<=mid:
            b[k] = arr[i]
            i+=1
            k+=1 
    while j<=high:
            b[k] = arr[j]
            j+=1
            k+=1                        
    for i in range(len(b)):
        arr[i+low] = b[i]    
        
arr = [19,3,9,12,4,19]
merge(arr,0,len(arr)-1)
print(arr)