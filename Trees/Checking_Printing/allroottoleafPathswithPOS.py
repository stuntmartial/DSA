class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def func(self):
        if self.root==None:
            return

        vl={self.root:0}
        paths=[]
        path=[]
        self.func_helper(self.root,vl,path,paths)

        for path in paths:
            disp(path)
            min_lev=99999
            for j in path:
                min_lev=min(min_lev,vl[j])
            op=''
            for j in path:
                op=op+'\n'+abs(vl[j]-min_lev)*'_'+j.val

            print(op)

    def func_helper(self,node,vl,path,paths):
        if node==None:
            return

        path.append(node)
        if node.left==None and node.right==None:
            p=[]
            for i in path:
                p.append(i)

            paths.append(p)
            path.pop(len(path)-1)
            return

        if node.left!=None:
            vl[node.left]=vl[node]-1
            self.func_helper(node.left,vl,path,paths)

        if node.right!=None:
            vl[node.right]=vl[node]+1
            self.func_helper(node.right,vl,path,paths)

        path.pop(len(path)-1)

def disp(path):
    if path==None:
        return

    for i in path:
        print(i.val,end='  ')
    print()

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

t=Tree(root)
t.func()