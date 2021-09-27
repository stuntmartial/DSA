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
        key1=str(node1)+str(node2)
        self.weights[key1]=weight
        self.edges+=1

    def func(self,src,dest,k):
        n=len(list(self.d.keys()))
    
        val_dict={src:0}
        for i in self.d.keys():
            if i!=src:
                val_dict[i]=1000

        edge_list=self.weights.keys()
        for i in range(k+1):
            for j in edge_list:
                node1=j[0];node2=j[1]
                if val_dict[node2]>val_dict[node1]+self.weights[j]:
                    val_dict[node2]=val_dict[node1]+self.weights[j]

        print(val_dict)

g=Graph()
g.add_edge('0','1',1)
g.add_edge('0','2',3)
g.add_edge('0','3',20)
g.add_edge('1','3',1)
g.add_edge('2','3',6)

g.func('0','3',2)