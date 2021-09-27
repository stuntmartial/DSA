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

    def sort_bitonic(self):
        if self.head==None:
            print('No nodes...')
            return

        ptr=self.head
        ptr1=self.head
        while ptr.right!=None:
            if ptr.val<=ptr.right.val:
                ptr=ptr.right

            else:
                break

        if ptr.right==None:
            return
        
        ptr2=ptr.right
        ptr2.left=None
        dll2=DLL(ptr.right)
        ptr.right=None

        dll2.reverse()
        self.merge(dll2)

    def merge(self,dll2):
        if dll2.head==None or self.head==None:
            print("No nodes...")
            return 

        dll3=DLL()
        ptr1=self.head
        ptr2=dll2.head
        count=0
        print(ptr2.val)
        while True:
            if ptr1==None or ptr2==None:
                break
            if ptr1.val <= ptr2.val:
                if count==0:
                    dll3.ins_beg(ptr1.val)
                else:
                    dll3.ins_end(ptr1.val)
                count+=1
                ptr1=ptr1.right
            else:
                if count==0:
                    dll3.ins_beg(ptr2.val)
                else:
                    dll3.ins_end(ptr2.val)
                count+=1
                ptr2=ptr2.right

            if ptr1==None:
                while ptr2!=None:
                    dll3.ins_end(ptr2.val)
                    ptr2=ptr2.right

            elif ptr2==None:
                while ptr1!=None:
                    dll3.ins_end(ptr1.val)
                    ptr1=ptr1.right

        disp(dll3.head)
                    
    def reverse(self):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        while ptr!=None:
            right=ptr.right
            ptr.left,ptr.right=ptr.right,ptr.left
            if right==None:
                self.head=ptr

            ptr=right


def disp(node):
    if node==None:
        print("NO nodes...")
        return
    
    ptr=node
    while ptr!=None:
        print(ptr.val,end=" ")
        ptr=ptr.right

    print()
        
dll=DLL()
dll.ins_beg(2)
dll.ins_end(5)
dll.ins_end(7)
dll.ins_end(12)
dll.ins_end(10)
dll.ins_end(6)
dll.ins_end(4)
dll.ins_end(1)

disp(dll.head)
dll.sort_bitonic()