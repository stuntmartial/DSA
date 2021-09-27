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

        global val_dict

    def floyd_warshall(self):
        node_list=list(self.d.keys())
        val_dict={i:0 for i in node_list}
        sp=[]
        for i in range(len(node_list)):
            sp.append([1000]*len(node_list))
        

        for i in range(len(node_list)):
            for j in range(len(node_list)):
                print(i,j)
                if i==j:
                    sp[i][j]=0
                elif str(i)+str(j) in self.weights.keys():
                    sp[i][j]=self.weights[str(i)+str(j)]
        
        for i in range(len(node_list)):
            print('(',i,')',end='\t')
        print()

        for i in range(len(node_list)):
            for j in range(len(node_list)):
                print(sp[i][j],end='\t')
            print()
        print()
        print()
        print()

        for k in range(len(node_list)):
            for i in range(len(node_list)):
                for j in range(len(node_list)):
                    sp[i][j]=min(sp[i][j],sp[i][k]+sp[k][j])
        
        for i in range(len(node_list)):
            print('(',i,')',end='\t')
        print()

        for i in range(len(node_list)):
            for j in range(len(node_list)):
                print(sp[i][j],end='\t')
            print()
        



g=Graph()
g.add_edge(0,1,3)
g.add_edge(0,2,10)
g.add_edge(0,5,1)
g.add_edge(1,2,6)
g.add_edge(1,3,1)
g.add_edge(2,3,1)
g.add_edge(3,6,4)
g.add_edge(4,3,1)
g.add_edge(5,6,1)
g.add_edge(3,5,10)
g.floyd_warshall()

        