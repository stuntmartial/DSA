class Graph:
    def __init__(self):
        self.d={}
        self.weights={}
        self.nodes=0
        self.edges=0
        self.additional_node_count=0

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

        if weight==1:
            self.d[node1].append(node2)
            key1=str(node1)+str(node2)
            self.weights[key1]=weight
            
        elif weight==2:
            additional_node='X'+str(self.additional_node_count)
            self.add_node(additional_node)
            self.additional_node_count+=1
            self.d[node1].append(additional_node)
            self.d[additional_node].append(node2)
            self.weights[node1+additional_node]=1
            self.weights[additional_node+node2]=1
            
        self.edges+=1

    def bfs(self,src,dest):
        print(self.weights)
        q=[src]
        visited_dict={src:1}
        val_dict={src:0}
        for i in self.d.keys():
            if i!=src:
                visited_dict[i]=0
                val_dict[i]=1000

        while len(q)>0:
            v=q.pop(0)
            for i in self.d[v]:
                if visited_dict[i]==0:
                    q.append(i)
                    visited_dict[i]=1
                    val_dict[i]=val_dict[v]+1
                    if i==dest:
                        print(val_dict)
                        return

g=Graph()
g.add_edge('0','1',2) 
g.add_edge('0','2',2) 
g.add_edge('1','2',1) 
g.add_edge('1','3',1) 
g.add_edge('2','0',1) 
g.add_edge('2','3',2) 
g.add_edge('3','3',2)

g.bfs('0','3')