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

    def reverse(self):
        if self.head==None:
            print("No nodes...")
            return

        self.reverse_helper(self.head)
        self.disp()

    def reverse_helper(self,node):
        if node==None:
            return

        nxt_node=node.right
        node.left,node.right=node.right,node.left
        self.reverse_helper(nxt_node)
        if nxt_node==None:
            self.head=node

    def disp(self):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        while ptr!=None:
            print(ptr.val)
            ptr=ptr.right
        

dll1=DLL()
'''
while True:
    ch=int(input("Enter choice...: \n"))

    if ch==1:
        node_val=int(input("Enter node_val : "))
        dll1.ins_beg(node_val)
        dll1.disp()

    elif ch==2:
        node_val=int(input("Enter node_val : "))
        dll1.ins_end(node_val)
        dll1.disp()

    elif ch==3:
        dll1.reverse()

    else:
        print("Terminating...")
        break
'''
dll1.ins_beg(10)
dll1.ins_end(20)
dll1.ins_end(30)
dll1.ins_end(40)
dll1.ins_end(50)
dll1.ins_end(60)

dll1.reverse()
print("After reversing....")
dll1.disp()