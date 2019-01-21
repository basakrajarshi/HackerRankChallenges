def checkBST(root):
    if root == None or (root.left == None and root.right == None):
        return(True)
    elif(root.right == None):
        return root.left.data < root.data and checkBST(root.left)
    elif(root.left == None):
        return root.right.data >= root.data and checkBST(root.right)
    return checkBST(root.left) and checkBST(root.right)
