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

    def bellmanford(self,node):
        if node not in self.d.keys():
            print('Node not present...')
            return

        edge_list=self.get_edge_list()
        print(edge_list)
        v=self.d.keys()
        val_dict={node:0}
        for i in self.d.keys():
            if i!=node:
                val_dict[i]=1000000000

        print(val_dict)
        for i in range(1,len(v)-1):
            flag=0
            for j in edge_list:
                node1=j[0];node2=j[1]
                print(val_dict[int(node1)])#,node2,self.weights[j])
                if val_dict[int(node2)] > val_dict[int(node1)]+self.weights[j]:
                    val_dict[int(node2)]=val_dict[int(node1)]+self.weights[j]
                    #parent_dict[node2]=node1
                    flag=1

            if flag==0:
                break
        
        if flag==1:
            for j in edge_list:
                node1=j[0];node2=j[1]
                if val_dict[node2] < val_dict[node1]+self.weights[j]:
                    val_dict[node2]=val_dict[node1]+self.weights[j]
                    parent_dict[node2]=node1
                    flag=2
                    break

        if flag==2:
            print('Negative edge weight cycle present')
        else:
            print(val_dict)

    def get_edge_list(self):
        return list(self.weights.keys())

g=Graph()
g.add_edge(1,0,3)
g.add_edge(1,4,1)
g.add_edge(1,2,9)
g.add_edge(1,3,7)
g.add_edge(0,3,1)
g.add_edge(0,2,3)
g.add_edge(4,6,1)
g.add_edge(6,5,1)
g.add_edge(5,2,1)
g.add_edge(3,2,1)

g.bellmanford(1)
        

        