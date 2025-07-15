def level_wise_height(root):
    if root ==None:
        return 0
    
    height = 1 # add 1 with height of child subtree
    max_height = 0 # used to keep the maximum height between all  childrens
    for eachchild in root.child:
        max_height = max(max_height,level_wise_height(eachchild))
    height = height+ max_height
    return height    