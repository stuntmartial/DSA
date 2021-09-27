class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def get_top_view(self):
        if self.root==None:
            return

        vertical_levels={0:[self.root]}
        vl_dict={self.root:0}
        q=[self.root]
        while len(q)>0:
            node=q.pop(0)
            if node.left!=None:
                vl_dict[node.left]=vl_dict[node]-1
                q.append(node.left)
                try:
                    vertical_levels[vl_dict[node.left]].append(node.left)
                except:
                    vertical_levels[vl_dict[node.left]]=[node.left]

            if node.right!=None:
                vl_dict[node.right]=vl_dict[node]+1
                q.append(node.right)
                try:
                    vertical_levels[vl_dict[node.right]].append(node.right)
                except:
                    vertical_levels[vl_dict[node.right]]=[node.right]



        keys=[i for i in vertical_levels.keys()]
        keys.sort()

        op=[]
        for i in keys:
            op.append(vertical_levels[i][0].val)

        print(op)





root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.right = Node(4) 
root.left.right.right = Node(5) 
root.left.right.right.right = Node(6) 
 
t=Tree(root)
t.get_top_view()