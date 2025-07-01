def selection(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[min]> arr[j]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr            


arr = [5,2,19,8,7,22,6,11]
print(selection(arr))