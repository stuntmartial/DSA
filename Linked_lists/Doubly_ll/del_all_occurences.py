class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class DLL:
    def __init__(self,head=None):
        self.head=head
        
    def ins_beg(self,node_val):
        if self.head==None:
            self.head=Node(node_val)

        else:
            node=Node(node_val)
            node.right=self.head
            self.head.left=node
            self.head=node

    def ins_end(self,node_val):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        while ptr.right!=None:
            ptr=ptr.right

        node=Node(node_val)
        ptr.right=node
        node.left=ptr

    def del_beg(self):
        if self.head==None:
            print("No nodes...")
            return

        nxt=self.head.right
        self.head.right=None
        self.head=nxt
        self.head.left=None

    def del_end(self):
        if self.head==None:
            print('No nodes...')
            return

        ptr=self.head
        while ptr.right!=None:
            ptr=ptr.right

        left=ptr.left
        ptr.left=None
        left.right=None

    def del_mid(self,node1,node,node2):
        if node1==None or node==None or node2==None:
            print('One or more nodes is null...')
            return

        ptr=self.head
        while ptr!=node1:
            ptr=ptr.right

        if ptr.right.right!=node2:
            print('node2 does not occur after node1')
            return

        node1.right=node2
        node2.left=node1
        node.right=None
        node.left=None

    def del_all_occ(self,node_val):
        ptr=self.head
        while ptr!=None:
            if ptr.val==node_val:
                if ptr.left==None:
                    print('Deleting beg')
                    self.del_beg()
                    ptr=self.head
                    continue

                elif ptr.right==None:
                    print('Deleting end')
                    self.del_end()
                else:
                    print('Deleting mid')
                    right=ptr.right
                    self.del_mid(ptr.left,ptr,ptr.right)
                    ptr=right
                    continue

            ptr=ptr.right
            
    def disp(self):
        if self.head==None:
            print('No nodes...')
            return 

        ptr=self.head
        while ptr!=None:
            print(ptr.val,end=" ")
            ptr=ptr.right

        print()

dl=DLL()
dl.ins_beg(1)
dl.ins_end(2)
dl.ins_end(2)
dl.ins_end(3)
dl.ins_end(1)
dl.ins_beg(1)
dl.disp()

dl.del_all_occ(1)
dl.disp()
