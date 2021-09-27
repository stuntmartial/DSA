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
        
    def add_edge(self,node1,node2,weight=0):
        if node1 not in self.d.keys():
            self.add_node(node1)
        if node2 not in self.d.keys():
            self.add_node(node2)

        self.d[node1].append(node2)
        key1=str(node1)+str(node2)
        self.weights[key1]=weight
        self.edges+=1

    def minRev(self,src,dest):
        self.rev()
        for i in self.weights.keys():
            print(i,": ",self.weights[i])

        n=self.bfs(src,dest)
        print(n)
        return n

    def rev(self):
        edge_list=[]
        for i in self.weights.keys():
            edge_list.append(i)

        for i in edge_list:
            self.add_edge(i[1],i[0],1)

    def bfs(self,src,dest):
        q=[src]
        visited_dict={src:1}
        cost={src:0}
        for i in self.d.keys():
            if i!=src:
                visited_dict[i]=0
                cost[i]=-1

        while len(q)>0:
            print('q----> ',q)
            v=q.pop(0)
            print('v: ',v,end='\t')
            for i in self.d[v]:
                if visited_dict[i]==0:
                    if self.weights[str(v)+str(i)]==0:
                        q.insert(0,i)
                    else:
                        q.append(i)
                    visited_dict[i]=1
                    cost[i]=cost[v]+self.weights[str(v)+str(i)]
                    print()
                    print('i-->',i,'cost-->',cost[i])
                    if i==dest:
                        print()
                        return cost

g=Graph()
g.add_edge('0','1')
g.add_edge('2','1')
g.add_edge('2','3')
g.add_edge('6','3')
g.add_edge('5','1')
g.add_edge('4','5')
g.add_edge('6','4')

g.minRev('0','6')

