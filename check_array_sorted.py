def sortedarr(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    if (arr[0]>arr[1]):
        return False
    else:
        return sortedarr(arr[1:])



print(sortedarr([8,2,19,32,11]))
print(sortedarr([10,20,30,40]))