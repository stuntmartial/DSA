class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def get_right_view(self):
        if self.root==None:
            return

        horizontal_levels={0:[self.root]}
        hl_dict={self.root:0}
        q=[self.root]
        while len(q)>0:
            node=q.pop(0)
            if node.left!=None:
                hl_dict[node.left]=hl_dict[node]+1
                q.append(node.left)
                try:
                    horizontal_levels[hl_dict[node.left]].append(node.left)
                except:
                    horizontal_levels[hl_dict[node.left]]=[node.left]

            if node.right!=None:
                hl_dict[node.right]=hl_dict[node]+1
                q.append(node.right)
                try:
                    horizontal_levels[hl_dict[node.right]].append(node.right)
                except:
                    horizontal_levels[hl_dict[node.right]]=[node.right]

        op=[]
        for i in horizontal_levels.keys():
            op.append(horizontal_levels[i][len(horizontal_levels[i])-1].val)

        print(op)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.right = Node(4) 
root.left.right.right = Node(5) 
root.left.right.right.right = Node(6) 
 
t=Tree(root)
t.get_right_view()