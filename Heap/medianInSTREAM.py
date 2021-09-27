class maxHeap:
    def __init__(self):
        self.heap = list()
        self.length=0
        
    def ins(self,ele):
        
        self.length+=1
        self.heap.append(ele)
        
        
        if self.length==1:
            return
        
        childIndex = self.length-1
        
        while childIndex!=0:
            parentIndex = (childIndex-1)//2
            
            if self.heap[childIndex]<=self.heap[parentIndex]:
                return
            
            self.heap[childIndex],self.heap[parentIndex] = self.heap[parentIndex],self.heap[childIndex]
            childIndex = parentIndex
        
        print('Heap after ins')
    def delete(self):
        
        delEle = self.heap[0]
        
        self.heap[0]=self.heap[self.length-1]
        self.heap.pop(self.length-1)
        self.length-=1
        
        parentIndex = 0
        while True:
            
            c1 = parentIndex*2 + 1 ; c2 = parentIndex*2 + 2
            
            if c1<self.length and c2<self.length:
                tmp = self.heap[parentIndex]
                self.heap[parentIndex] = max(self.heap[parentIndex],self.heap[c1],self.heap[c2])
                
                if self.heap[parentIndex] == tmp:
                    return
                elif self.heap[parentIndex] == self.heap[c1]:
                    self.heap[c1]=tmp
                    parentIndex = c1
                    continue
                elif self.heap[parentIndex] == self.heap[c2]:
                    self.heap[c2]=tmp
                    parentIndex = c2
                    continue
                
            elif c1<self.length:
                tmp = self.heap[parentIndex]
                self.heap[parentIndex] = max(self.heap[parentIndex],self.heap[c1])
                if self.heap[parentIndex] == tmp:
                    return
                elif self.heap[parentIndex] == self.heap[c1]:
                    self.heap[c1] = tmp
                    parentIndex = c1
                    continue
                
            elif c2<self.length:
                tmp = self.heap[parentIndex]
                self.heap[parentIndex] = max(self.heap[parentIndex],self.heap[c2])
                if self.heap[parentIndex] == tmp:
                    return
                elif self.heap[parentIndex] == self.heap[c2]:
                    self.heap[c2] = tmp
                    parentIndex = c2
                    continue
            else:
                break

class minHeap:
    def __init__(self):
        self.heap = list()
        self.length=0
        
    def ins(self,ele):
        
        self.length+=1
        self.heap.append(ele)
        
        if self.length==1:
            return
        
        childIndex = self.length-1
        
        while childIndex!=0:
            parentIndex = (childIndex-1)//2
            
            if self.heap[childIndex]>=self.heap[parentIndex]:
                return
            
            self.heap[childIndex],self.heap[parentIndex] = self.heap[parentIndex],self.heap[childIndex]
            childIndex = parentIndex
            
    def delete(self):
        
        delEle = self.heap[0]
        
        self.heap[0]=self.heap[self.length-1]
        self.heap.pop(self.length-1)
        self.length-=1
        
        parentIndex = 0
        while True:
            
            c1 = parentIndex*2 + 1 ; c2 = parentIndex*2 + 2
            
            if c1<self.length and c2<self.length:
                tmp = self.heap[parentIndex]
                self.heap[parentIndex] = min(self.heap[parentIndex],self.heap[c1],self.heap[c2])
                
                if self.heap[parentIndex] == tmp:
                    return
                elif self.heap[parentIndex] == self.heap[c1]:
                    self.heap[c1]=tmp
                    parentIndex = c1
                    continue
                elif self.heap[parentIndex] == self.heap[c2]:
                    self.heap[c2]=tmp
                    parentIndex = c2
                    continue
                
            elif c1<self.length:
                tmp = self.heap[parentIndex]
                self.heap[parentIndex] = min(self.heap[parentIndex],self.heap[c1])
                if self.heap[parentIndex] == tmp:
                    return
                elif self.heap[parentIndex] == self.heap[c1]:
                    self.heap[c1] = tmp
                    parentIndex = c1
                    continue
                
            elif c2<self.length:
                tmp = self.heap[parentIndex]
                self.heap[parentIndex] = min(self.heap[parentIndex],self.heap[c2])
                if self.heap[parentIndex] == tmp:
                    return
                elif self.heap[parentIndex] == self.heap[c2]:
                    self.heap[c2] = tmp
                    parentIndex = c2
                    continue
            else:
                break

                
class MedianFinder:

    def __init__(self):
        self.leftHeap = maxHeap()
        self.rightHeap = minHeap()

    def addNum(self, num: int) -> None:
        
        if self.leftHeap.length==0 or num<self.leftHeap.heap[0]:
            self.leftHeap.ins(num)
        else:
            self.rightHeap.ins(num)
            
        if (self.leftHeap.length-self.rightHeap.length) > 1:
            ele = self.leftHeap.heap[0]
            self.leftHeap.delete()
            self.rightHeap.ins(ele)
            
        if (self.rightHeap.length-self.leftHeap.length) > 1:
            ele = self.rightHeap.heap[0]
            self.rightHeap.delete()
            self.leftHeap.ins(ele)
            

    def findMedian(self) -> float:
        
        
        
        if self.leftHeap.length == self.rightHeap.length:
            return ( self.leftHeap.heap[0] + self.rightHeap.heap[0] ) /2
        elif self.leftHeap.length > self.rightHeap.length:
            return self.leftHeap.heap[0]
        else:
            return self.rightHeap.heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()