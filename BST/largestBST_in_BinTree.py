class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val;self.left=left;self.right=right

def getLargest(node):
    if node==None:return True,0,float("-inf"),float("inf") #Bst Stat, Size, Max down, Min Down
    
    leftStat,leftSize,leftMax,leftMin=getLargest(node.left)
    rightStat,rightSize,rightMax,rightMin=getLargest(node.right)

    if leftStat and rightStat:
        if node.val>=leftMax and node.val<=rightMin:
            return True,1+leftSize+rightSize,max(node.val,rightMax),min(node.val,leftMin)
        else:
            return False,max(leftSize,rightSize),float("-inf"),float("inf")
    
    elif not leftStat and not rightStat:
        return False,max(leftSize,rightSize),float("-inf"),float("inf")
    elif leftStat:
        return False,leftSize,float("-inf"),float("inf")
    elif rightStat:
        return False,rightSize,float("-inf"),float("inf")

root=Node(1)
root.left=Node(4)
root.right=Node(4)
root.left.left=Node(6)
root.left.right=Node(8)

print(getLargest(root))

root=Node(50)
root.left=Node(30)
root.right=Node(60)
root.left.left=Node(5)
root.left.right=Node(20)
root.right.left=Node(45)
root.right.right=Node(70)
root.right.right.left=Node(65)
root.right.right.right=Node(80)

print(getLargest(root))