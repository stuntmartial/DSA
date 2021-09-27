class ll_Node:
    def __init__(self,val,nxt=None):
        self.val=val
        self.nxt=nxt

class tree_Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
class LL:
    def __init__(self,head=None):
        self.head=head

    def create_tree(self):
        if self.head==None:
            return None

        ptr=self.head
        root=tree_Node(self.head.val)
        q=[root]
        t=Tree(root)
        while len(q)>0:
            v=q.pop(0)

            ptr=ptr.nxt
            if ptr!=None:
                node=tree_Node(ptr.val)
                q.append(node)
                v.left=node
            elif ptr==None:
                break

            ptr=ptr.nxt
            if ptr!=None:
                node=tree_Node(ptr.val)
                q.append(node)
                v.right=node
            elif ptr==None:
                break
            
        t.preordr()

class Tree:
    def __init__(self,root):
        self.root=root

    def preordr(self):
        if self.root==None:
            return

        self.func2(self.root)

    def func2(self,node):
        if node==None:
            return

        print(node.val)
        self.func2(node.left)
        self.func2(node.right)

head=ll_Node(10)
head.nxt=ll_Node(12)
head.nxt.nxt=ll_Node(15)
head.nxt.nxt.nxt=ll_Node(25)
head.nxt.nxt.nxt.nxt=ll_Node(30)
head.nxt.nxt.nxt.nxt.nxt=ll_Node(36)

ll1=LL(head)
ll1.create_tree()