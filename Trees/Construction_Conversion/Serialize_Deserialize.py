class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def dfs(node):
    if node==None:
        return 
    
    print(node.val)
    dfs(node.left)
    dfs(node.right)

def serializeHelper(node,serializedString):
    if node==None:
        serializedString.append("X")
        return 

    serializedString.append(node.val)
    print(node.val,serializedString)
    serializeHelper(node.left,serializedString)
    serializeHelper(node.right,serializedString)

def serialize(root):
    if root==None:
        return ""

    serializedString=[]
    serializeHelper(root,serializedString)
    print(serializedString)
    return serializedString

def deserialize(serializedString,index):
    if index[0]==len(serializedString):
        return None
        
    if serializedString[index[0]]=="X":
        index[0]+=1
        return None

    node=serializedString[index[0]]
    node=Node(val=node)
    index[0]+=1
    node.left=deserialize(serializedString,index)
    node.right=deserialize(serializedString,index)

    return node

root=Node('1')
root.left=Node('2')
root.right=Node('4')
root.left.right=Node('3')
root.right.left=Node('5')

serializedString=serialize(root)
rootRetrieved=deserialize(serializedString,[0])
dfs(rootRetrieved)