def Node(self,val,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right

def chkSubtree(root1,root2):
    ser1=serialize(root1)
    ser2=serialize(root2)

    #chk if ser2 in ser1
    #KMP on list
    #return True if OK
    #return False otherwise