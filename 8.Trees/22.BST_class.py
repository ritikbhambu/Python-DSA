class BST_node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None



    def delete(self,data):
        pass
    
    def search(self,data): # assuming user has not entered the root
        return self.search_helper(data,root) # calling a helper function which accepts root
    

    def search_helper(self,data,root):
        if root is None:
            return False
        
        if self.data==root.data:
            return True
        
        if self.data < root.data:
            return self.search_helper(data,root.left)
        else:
            return self.search_helper(data,root.right)


    def insert(self,data):
        self.root = self.insert_helper(data,root)
        return self.root 
    
    def insert_helper(self,data,root):
        if root==None:
            newnode = BST(data)
            return newnode
        if data < root.data:
            root.left = self.insert_helper(data,root.left) 
        else:
            root.right = self.insert_helper(data,root.right)   



root = BST()
root.insert(10)
root.insert(20)
root.insert(9)
root.insert(7)