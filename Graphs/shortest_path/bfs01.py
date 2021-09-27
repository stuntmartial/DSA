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

    def func(self,src):
        q=[src]
        visited_dict={src:1}
        val_dict={src:0}
        for i in self.d.keys():
            if i!=src:
                val_dict[i]=1000
                visited_dict[i]=0

        while len(q)>0:
            v=q.pop(0)
            for i in self.d[v]:
                if visited_dict[i]==0:
                    visited_dict[i]=1
                    if self.weights[v+i]==0:
                        q.insert(0,i)
                        val_dict[i]=val_dict[v]
                    elif self.weights[v+i]==1:
                        q.append(i)
                        val_dict[i]=val_dict[v]+1
        
        print(val_dict)


g=Graph()
g.add_edge('0','1',0) 
g.add_edge('0','7',1)
g.add_edge('1','7',1)
g.add_edge('1','2',1)
g.add_edge('2','3',0)
g.add_edge('2','5',0)
g.add_edge('2','8',1)
g.add_edge('3','4',1)
g.add_edge('3','5',1)
g.add_edge('4','5',1)
g.add_edge('5','6',1)
g.add_edge('6','7',1)
g.add_edge('7','8',1)
g.func('0')