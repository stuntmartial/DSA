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

    def find_pair(self,target_sum):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        ht={}
        while ptr!=None:
            try:
                ht[target_sum-ptr.val].append(ptr.val)
            except:
                ht[ptr.val]=[]

            ptr=ptr.right

        for i in list(ht.keys()):
            print(i," : ",ht[i])

dll1=DLL()
dll1.ins_beg(5)
dll1.ins_end(1)
dll1.ins_end(2)
dll1.ins_end(0)
dll1.ins_end(3)
dll1.ins_end(4)
dll1.ins_end(6)

dll1.find_pair(int(input("Enter target_sum : ")))