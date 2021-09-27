class Heap_Node:
    def __init__(self,node_val,arr_id,index):
        self.node_val=node_val
        self.arr_id=arr_id
        self.index=index

class Heap():
    def __init__(self,length):
        self.length=length

    def heapify(self):

    def insert(self):

    def pop(self):


def func(matrix):
    heap=Heap(length=len(matrix[0]))
    op=list()
    next_index_i=None
    next_index_j=None

    for i in range(len(matrix)):
        node_val=Heap_Node(
            node_val=matrix[i][0]
            arr_id=i
            index=0
        )

        heap.insert(node_val)

    while heap.empty() is False:
        heap_node=heap.pop()
        op.append(heap_node.node_val)
        next_index_i=heap_node.arr_id
        next_index_j=heap_node.index+1

        if next_index_i<len(matrix):
            if next_index_j<len(matrix[0]):
                heap_node=Heap_Node(node_val=matrix[next_index_i][next_index_j],arr_id=next_index_i,index=next_index_j)
        
    print(op)
