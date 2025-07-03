notebook = [] #globally defined list

def appendglobal(arr,x,index):

    if index==len(arr):
        return
    
    if arr[index]==x:
        notebook.append(index) 

    appendglobal(arr,x,index+1)
   

appendglobal([10,5,9,3,6,5,8],5,0)
print(notebook)