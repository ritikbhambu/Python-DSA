class BstNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


#-------------------------
def find_max(root):
    if root is None:  #If you return 0 when a node is None, and all values in your tree are negative, the result would be wrong.
        return float("-inf") # It behaves like a very small number,smaller than any real number
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(left_max,right_max,root.data)        


def find_min(root):
    if root is None:  #If you return 0 when a node is None, and all values in your tree are negative, the result would be wrong.
        return float("+inf") # It behaves like a very big number,bigger than any real number
    left_min = find_min(root.left)
    right_min = find_min(root.right)
    return min(left_min,right_min,root.data)


def is_bst(root):
    if root is None:
        return True  # empty tree is a bst
    
    left_max = find_max(root.left)
    right_min = find_min(root.right)
    
    left_bst = is_bst(root.left)
    right_bst = is_bst(root.right)

    ans = left_bst and right_bst and (left_max<root.data and right_min>root.data)
    return ans