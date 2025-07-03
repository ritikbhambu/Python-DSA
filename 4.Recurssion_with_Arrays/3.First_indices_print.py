def firstnlast(arr,x,index):

    # if len(arr)==0: #its not requird as we are not slicing the array so this condition will never occur
    #     return -1
    
    if index == len(arr)-1:
        return 
    if arr[index]==x:   # compare x with every increased index value
        print(index)
    small = firstnlast(arr,x,index+1)  #pass the next index every time

firstnlast([10,9,3,5,7,9,8],9,0)