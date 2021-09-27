class Solution:
    def FirstNonRepeating(self, A):
        if len(A)==1:
            return A[0]
            
        NR_dict=dict();ans=list()
        stream=DLL()
        
        for ch in A:
            if ch in NR_dict.keys():
                if NR_dict[ch]:
	                stream.delNode(ch);ans.append(stream.retHead());NR_dict[ch]=False
                else:
                    ans.append(stream.retHead())
            else:
                stream.ins(ch);NR_dict[ch]=True;ans.append(stream.retHead())
	    
        return "".join(ans)
		
class Node:
    def __init__(self,val=None,prev=None,nxt=None):
        self.val=val;self.prev=prev;self.nxt=nxt
        
class DLL:
    def __init__(self,head=None,tail=None):
        self.head=head;self.tail=tail;
        self.ptrs=dict()
        
    def retHead(self):
        if self.head==None:
            return "#"
        else:
            return self.head.val
            
    def ins(self,val):
        node=Node(val)
        if self.head==None:
            self.head=node;self.tail=node
        else:    
            self.tail.nxt=node;node.prev=self.tail;self.tail=node
            
        self.ptrs[val]=node
        
    def delNode(self,char):
        node=self.ptrs[char]
        prev=node.prev;nxt=node.nxt
        
        if prev==None:
            if nxt==None:
                self.head=None;self.tail=None
            else:    
                nxt.prev=None;self.head.nxt=None;self.head=nxt
            
        elif nxt==None:
            prev.nxt=None;self.tail.prev=None;self.tail=prev
            
        else:
            node.prev=None;node.nxt=None;prev.nxt=nxt;nxt.prev=prev
            
        self.ptrs.pop(char)
        
s=Solution()
op=s.FirstNonRepeating(input("Enter string : "))
print(op)