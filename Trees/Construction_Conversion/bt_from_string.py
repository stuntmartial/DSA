index=0
digits=[str(i) for i in range(0,10)]
class Node:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

def construct(s):
    global index
    index=0

    root=func(s)
    return root

def func(s):
    global index,digits

    if index>=len(s):
        return

    if s[index] in digits:
        node=Node(s[index])
        if index+1>=len(s):
            return
        if s[index+1]=='(':
            if node.left is None:
                index+=2
                node.left=func(s)
            elif node.right is None:
                index+=1
                node.right=func(s)
            else:
                print('Error')
                exit()

        if s[index]=='(':
            if node.right is not None:
                print('Error')
                exit()


                NOT DONEEEEEEEEEEEEE

            







    if s[index]=='(':

        if s[index+1]==')':
            index+=1
            return

        elif s[index+1] in digits:

