def append_and_return(arr,x,index):

    if index==len(arr):
        return []
    
    notebook = append_and_return(arr,x,index+1)  # at the end gives us empty list 
                                                 # which can fill using below if condition

    if arr[index]==x:
        notebook.append(index) # as we are appending after all function calls the retuned list can contain reversed indexes
        return notebook        
    
    return notebook 

notebook = append_and_return([5,9,11,7,9,8],9,0)
print(notebook)
