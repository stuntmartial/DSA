#User function Template for python3

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if head==None:
            return 
        
        zero_head=None;zero_pos=None
        one_head=None;one_pos=None
        two_head=None;two_pos=None
        
        ptr=head
        while ptr!=None:
            if ptr.data==0:
                if zero_head==None:
                    zero_head=ptr
                    zero_pos=ptr
                else:
                    zero_pos.next=ptr
                    zero_pos=zero_pos.next
                    
            elif ptr.data==1:
                if one_head==None:
                    one_head=ptr
                    one_pos=ptr
                else:
                    one_pos.next=ptr
                    one_pos=one_pos.next
            
            elif ptr.data==2:
                if two_head==None:
                    two_head=ptr
                    two_pos=ptr
                else:
                    two_pos.next=ptr
                    two_pos=two_pos.next
            
                    
            ptr=ptr.next
        
        if zero_head!=None:
            head=zero_head
            if one_head!=None:
                zero_pos.next=one_head
                one_pos.next=two_head
                if two_pos!=None:
                    two_pos.next=None
            else:
                zero_pos.next=two_head
                if two_pos!=None:
                    two_pos.next=None
                
        elif one_head!=None:
            head=one_head
            one_pos.next=two_head
            if two_pos!=None:
                two_pos.next=None
        
        elif two_head!=None:
            head=two_head
            
        return head
            
        return head
                    
                    
