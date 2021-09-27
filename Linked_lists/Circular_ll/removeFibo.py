class Node:
    def __init__(self,val,nxt=None):
        self.val=val
        self.nxt=nxt

class circular_ll:
    def __init__(self,head=None):
        self.head=head
        if self.head==None:
            self.nodes=0
        else:
            self.nodes=1

    def add_beg(self,node):
        if self.head==None:
            node=Node(node)
            node.nxt=node
            self.head=node
            return

        ptr=self.head
        node=Node(node)
        while ptr.nxt!=self.head:
            ptr=ptr.nxt

        node.nxt=self.head
        self.head=node
        ptr.nxt=self.head

    def add_end(self,node):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        node=Node(node)
        while ptr.nxt!=self.head:
            ptr=ptr.nxt

        ptr.nxt=node
        node.nxt=self.head

    def delete_beg(self):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        while ptr.nxt != self.head:
            ptr=ptr.nxt

        head_nxt=self.head.nxt
        ptr.nxt=self.head.nxt
        self.head.nxt=None
        self.head=head_nxt

    def delete_end(self):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        while ptr.nxt.nxt!=self.head:
            ptr=ptr.nxt

        ptr_nxt=ptr.nxt
        ptr_nxt.nxt=None
        ptr.nxt=self.head
        
    def delete_fibo_nodes(self):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        max_val=0
        while ptr.nxt!=self.head:
            max_val=max(max_val,ptr.val)
            ptr=ptr.nxt

        fibo_list=generate_fibo(max_val)
        print(max_val,fibo_list)
        ptr=self.head
        prev=None
        while ptr.nxt !=self.head:
            
            print('ptr.val----> ',ptr.val)
            if ptr.val in fibo_list:
                print('Removing ',ptr.val)
                if ptr==self.head:
                    self.delete_beg()
                    ptr=self.head
                else:
                    prev.nxt=ptr.nxt
                    ptr.nxt=None
                    ptr=prev.nxt
                    if ptr==self.head:
                        break
                    else:
                        continue
                    
            prev=ptr
            ptr=ptr.nxt

        if ptr.val in fibo_list:
            prev.nxt=self.head
            ptr.nxt=None

        ptr=self.head
        print("Required linked list....")
        while ptr.nxt !=self.head:
            print(ptr.val,end=" ")
            ptr=ptr.nxt
        print(ptr.val)

    def disp(self):
        if self.head==None:
            print("No nodes...")
            return

        ptr=self.head
        while ptr.nxt!=self.head:
            print(ptr.val,end=" ")
            ptr=ptr.nxt
        print(ptr.val)

def generate_fibo(max_val):
    arr=[0,1]
    while arr[len(arr)-1] < max_val:
        val=arr[len(arr)-1]+arr[len(arr)-2]
        arr.append(val)

    return arr
        
cl=circular_ll()
cl.add_beg(1)
cl.disp()
cl.add_end(11)
cl.add_end(34)
cl.add_end(6)
cl.add_end(13)
cl.add_end(21)
cl.disp()
cl.delete_fibo_nodes()
cl.disp()