 
class BstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return BstNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

def find_min(node): # in right subtree we know that min always on left side
    while node.left is not None: # so traverse through left until its none and return last left value
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return None
    
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Node found
        if root.left is None and root.right is None:
            return None  # Case 1: No child
        
        elif root.left is None: # Case 2: One right child
            return root.right  # if left is none than delete the root and return right subtree
        
        elif root.right is None: # Case 2: One left child
            return root.left  # if right is none than delte the root and return left subtree
        else:
            # Case 3: Two children
            # approach1 - we can either replace the root with maximum value from the left subtree
            # approach2- or we can replace the minimum value from the right side . 
            # we are using approach 2 here
            min_node = find_min(root.right) # find min from right
            root.data = min_node.data # replace the root with min 
            root.right = delete(root.right, min_node.data) # delete the node which we used as replacemet from the right subtree
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)




# Create the BST
root = None
values = [10, 5, 15, 3, 7, 12, 18]
for val in values:
    root = insert(root, val)

print("Inorder traversal:")
inorder(root)

# Search for a value
print("\n\nSearch for 7:", search(root, 7))   # True
print("Search for 100:", search(root, 100))  # False

# Delete a value
root = delete(root, 10)  # Delete root node
print("\nInorder after deleting 10:")
inorder(root)
