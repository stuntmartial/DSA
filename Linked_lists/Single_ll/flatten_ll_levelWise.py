class Node:
    def __init__(self,val=0,nxt=None,down=None):
        self.val=val
        self.nxt=nxt
        self.down=down

def flatten(head):
    if head==None:
        return head

    queue=[head]
    while len(queue)>0:
        curr_node = queue.pop(0)
        if curr_node!=head:
            ptr.nxt = curr_node
        ptr = curr_node
        while ptr.nxt!=None:
            if ptr.down!=None:
                queue.append(ptr.down)
            ptr = ptr.nxt
        if ptr.down!=None:
            queue.append(ptr.down)

    ptr=head
    while ptr!=None:
        print(ptr.val,end='->')
        ptr.down=None
        ptr=ptr.nxt
    print('None')
    print()

head=Node(10)
head.nxt=Node(5)
head.nxt.nxt=Node(12)
head.nxt.nxt.nxt=Node(7)
head.nxt.nxt.nxt.nxt=Node(11)
head.down=Node(4)
head.down.nxt=Node(20)
head.down.nxt.nxt=Node(13)
head.down.nxt.down=Node(2)
head.down.nxt.nxt.down=Node(16)
head.down.nxt.nxt.down.down=Node(3)
head.nxt.nxt.nxt.down=Node(17)
head.nxt.nxt.nxt.down.nxt=Node(6)
head.nxt.nxt.nxt.down.down=Node(9)
head.nxt.nxt.nxt.down.down.nxt=Node(8)
head.nxt.nxt.nxt.down.down.down=Node(19)
head.nxt.nxt.nxt.down.down.down.nxt=Node(15)

flatten(head)