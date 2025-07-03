def Bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

arr = [ 10,4,9,15,7,11,2]
print(Bubble(arr))
