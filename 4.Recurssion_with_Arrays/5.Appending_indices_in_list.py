def appendindice(arr,x,index,notebook):
     
    if index==len(arr): # not slicing so no len==0 case
        return
    if arr[index]==x:
        notebook.append(index)
    appendindice(arr,x,index+1,notebook)   # everytime the updated notebook is provided to the function



notebook = []
appendindice([9,4,15,4,7,8],4,0,notebook)  # array,num to find,index,emptylist
print(notebook)