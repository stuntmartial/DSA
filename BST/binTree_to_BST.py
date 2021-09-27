class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val;self.left=left;self.right=right

def convert_to_BST(root):
    inOrder=getInOrder(root)
    sortedInOrder=sorted(inOrder)
    index=[0]
    root=createBST(root,sortedInOrder,index)
    return root
        
def getInOrder(node):
    if node==None:return list()
    
    inOrder=list()
    getInOrderUtil(node,inOrder)
    return inOrder
    
def getInOrderUtil(node,inOrder):
    if node==None:return None
    
    getInOrderUtil(node.left,inOrder)
    inOrder.append(node.val)
    getInOrderUtil(node.right,inOrder)
    
def createBST(node,sortedInOrder,index):
    if node==None:return None
    if index[0]==len(sortedInOrder):return None
    
    createBST(node.left,sortedInOrder,index)
    if index[0]==len(sortedInOrder):return None
    node.val=sortedInOrder[index[0]];index[0]+=1
    createBST(node.right,sortedInOrder,index)
    
    return node

root=Node(10)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(8)
root.left.right=Node(4)

root2=Node(10)
root2.left=Node(30)
root2.right=Node(15)
root2.left.left=Node(20)
root2.right.right=Node(5)

root_=convert_to_BST(root)
print(getInOrder(root_))

root2_=convert_to_BST(root2)
print(getInOrder(root2_))