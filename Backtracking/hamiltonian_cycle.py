class graph:
    
    def __init__(self):
        self.d={}
        self.nodes=0
        self.edges=0
        self.node_list=[]
        self.first_node=None
        
    def add_node(self,node):
        if node not in self.d.keys():
            self.d[node]=[]
            self.nodes+=1
            self.node_list.append(node)
            if self.nodes==1:
                self.first_node=node
            
    def add_edge(self,node1,node2):
        if node1 not in self.d.keys():
            self.add_node(node1)
        if node2 not in self.d.keys():
            self.add_node(node2)
            
        if node2 not in self.d[node1]:
            self.d[node1].append(node2)
            self.d[node2].append(node1)
            
    def issafe(self,cycle,node,pos):
        if node not in cycle and node in self.d[cycle[pos-1]]:
            return True
        else:
            return False
    
    def hp_helper(self,cycle,pos):
        
        if pos==self.nodes:
            if cycle[pos-1] in self.d[self.first_node]:
                return True
            else:
                return False
        
        for i in self.node_list:
            
            if self.issafe(cycle,i,pos):
                cycle[pos]=i
                if self.hp_helper(cycle,pos+1)==True:
                    return True
                cycle[pos]=-1
                    
        return False
        
        
    def hp(self):
        cycle=[-1]*self.nodes
        cycle[0]=self.first_node
        
        if self.hp_helper(cycle,1)==True:
            return 1
        else:
            return 0
        
        
T=int(input())
oplist=[]
for i in range(T):
    l=[int(i) for i in input().split()]
    g=graph()
    l=[i for i in input().split()]
    j=0
    while j<len(l)-1:
        g.add_edge(l[j],l[j+1])
        j+=2
    oplist.append(g.hp())    
    
for i in range(T):
    print(oplist[i])