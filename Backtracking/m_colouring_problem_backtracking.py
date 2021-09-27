class graph:
    
    def __init__(self):
        self.d={}
        self.nodes=0
        self.edges=0
        
    def add_node(self,node):
        if node not in self.d.keys():
            self.d[node]=[]
            self.nodes+=1
            
    def add_edge(self,node1,node2):
        if node1 not in self.d.keys():
            self.add_node(node1)
        if node2 not in self.d.keys():
            self.add_node(node2)
            
        self.d[node1].append(node2)
        self.d[node2].append(node1)
        
    def issafe(self,v,color,c):
        print(self.d[v])
        for i in self.d[v]:
            if color[i]==c:
                return False
        return True
        
    def mcol_helper(self,m,color,v):
        if v==self.nodes:
            return True
                
        for i in range(1,m+1):
            if self.issafe(v,color,i):
                color[v]=i
                if self.mcol_helper(m,color,v+1)==True:
                    return True
                color[v]=0
        
    def m_col(self,m):
        color=[0]*self.nodes
        if self.mcol_helper(m,color,0)==True:
            return 1
        else:
            return 0
        

 nodes=int(input())
 m=int(input())
 edges=int(input())
 edge_list=[int(i)-1 for i in input().split()]
 g=graph()
 j=0
 while j< len(edge_list):
    g.add_edge(edge_list[j],edge_list[j+1])
    j+=2
    
op=g.m_col(m)
print(op)
