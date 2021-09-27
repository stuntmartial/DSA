class Graph:
    def __init__(self):
        self.d={}
        self.weights={}
        self.nodes=0
        self.edges=0

    def add_node(self,node):
        if node in self.d.keys():
            return

        self.d[node]=[]
        self.nodes+=1
        
    def add_edge(self,node1,node2,weight):
        if node1 not in self.d.keys():
            self.add_node(node1)
        if node2 not in self.d.keys():
            self.add_node(node2)

        self.d[node1].append(node2)
        self.d[node2].append(node1)
        key1=str(node1)+str(node2)
        key2=str(node2)+str(node1)
        self.weights[key1]=weight
        self.weights[key2]=weight

        self.edges+=1

    def mst(self):
    
        self.weights={k: v for k, v in sorted(self.weights.items(), key=lambda item: item[1])}

        g=Graph()
        ds=Disjoint_Set(list(self.d.keys()))

        for i in self.weights.keys():
            node1=i[0]
            node2=i[1]

            if ds.find_path_compress(node1)==ds.find_path_compress(node2):
                continue
            else:
                ds.union_rank(ds.find_path_compress(node1),ds.find_path_compress(node2))
                g.add_edge(node1,node2,self.weights[i])

        print(g.d)
            
class Disjoint_Set:
    def __init__(self,arr):
        self.arr=arr
        self.parent={i:i for i in self.arr}
        self.rank={i:0 for i in self.arr}

    def find_path_compress(self,ele):
        if ele==self.parent[ele]:
            print(ele)
            return self.parent[ele]

        par=self.find_path_compress(self.parent[ele])
        self.parent[ele]=par
        return par

    def union_rank(self,ele1,ele2):
        parent_ele1=self.find_path_compress(ele1)
        parent_ele2=self.find_path_compress(ele2)

        if parent_ele1==parent_ele2:
            return

        if self.rank[parent_ele1]==self.rank[parent_ele2]:
            self.rank[parent_ele2]+=self.rank[parent_ele1]
            self.parent[parent_ele1]=parent_ele2

        elif self.rank[parent_ele1]>self.rank[parent_ele2]:
            self.parent[parent_ele2]=parent_ele1
            self.rank[parent_ele1]+=self.rank[parent_ele2]

        elif self.rank[parent_ele2]>self.rank[parent_ele1]:
            self.parent[parent_ele1]=parent_ele2
            self.rank[parent_ele2]+=self.rank[parent_ele1]

g=Graph()
g.add_edge('A','B',10)
g.add_edge('A','C',20)
g.add_edge('B','C',30)
g.add_edge('B','D',5)
g.add_edge('C','D',15)
g.add_edge('C','E',6)
g.add_edge('D','E',8)

print(g.d)
print(g.weights)
g.mst()