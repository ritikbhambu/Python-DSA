def sumarr(arr):
    if len(arr) ==0:
        return 0
    if len(arr)==1:
        return arr[0]
    value = arr[0] + sumarr(arr[1:]) 
     

    return value 
    

print(sumarr([10,20,30,5,7]))
print(sumarr([]))