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

    def swap(self,k):
        if k<=0:
            print("Enter valid k >= 1")
            return

        ptr=self.head
        count=1
        while True:
        
            if count==k:
                first_node_ref=ptr
                second_node_ref=self.head
            elif count>k:
                second_node_ref=second_node_ref.right
                

            ptr=ptr.right
            if ptr==None:
                break
            count+=1

        if count<k:
            print('k is larger than length...')
            return 

        print(first_node_ref.val,second_node_ref.val)

        if k==1 :
            first_node_ref.right.left=second_node_ref
            second_node_ref.left.right=first_node_ref
            first_node_ref.left=second_node_ref.left
            second_node_ref.right=first_node_ref.right
            first_node_ref.right=None
            second_node_ref.left=None
            self.head=second_node_ref
            self.disp()
            return

        elif k==count:
            first_node_ref.left.right=second_node_ref
            second_node_ref.right.left=first_node_ref
            first_node_ref.right=second_node_ref.right
            second_node_ref.left=first_node_ref.left
            first_node_ref.left=None
            second_node_ref.right=None
            self.head=first_node_ref
            self.disp()
            return

        first_node_ref.left.right=second_node_ref
        second_node_ref.left.right=first_node_ref
        first_node_ref.right.left=second_node_ref
        second_node_ref.right.left=first_node_ref

        first_node_ref.left,second_node_ref.left=second_node_ref.left,first_node_ref.left
        first_node_ref.right,second_node_ref.right=second_node_ref.right,first_node_ref.right

        self.disp()
        
    def disp(self):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        while ptr!=None:
            print(ptr.val)
            ptr=ptr.right
        

dll1=DLL()
dll1.ins_beg(10)
dll1.ins_end(20)
dll1.ins_end(30)
dll1.ins_end(40)
dll1.ins_end(50)
#dll1.ins_end(60)
dll1.disp()

dll1.swap(int(input("Enter k : ")))
            
