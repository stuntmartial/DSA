cycle_flag=0
class Graph:
    def __init__(self):
        self.d={}
        self.nodes=0
        self.edges=0

    def add_node(self,node):
        if node==None:
            return

        if node not in self.d.keys():
            self.d[node]=[]
            self.nodes+=1

    def add_edge(self,node1,node2):
        if node1 not in self.d.keys():
            self.add_node(node1)
        if node2 not in self.d.keys():
            self.add_node(node2)

        if node1 in self.d[node2]:
            return

        if node1 not in self.d[node2]:
            self.d[node2].append(node1)
        if node2 not in self.d[node1]:
            self.d[node1].append(node2)

        self.edges+=1
        
def chkTree(g):
    global cycle_flag

    visited_dict={i:0 for i in g.d.keys()}
    parent_dict={i:None for i in g.d.keys()}
    cycle_flag=0
    traverse(g,list(g.d.keys())[0],visited_dict,parent_dict)

    if cycle_flag==0:
        for i in visited_dict.keys():
            if visited_dict[i]==0:
                print('No')
                return
        
        print('Yes')
    else:
        print('No')

def traverse(g,node,visited_dict,parent_dict):
    global cycle_flag

    print(node)
    visited_dict[node]=1
    print(visited_dict)
    for i in g.d[node]:
        print('i--->',i)
        if visited_dict[i]==0:
            parent_dict[i]=node
            traverse(g,i,visited_dict,parent_dict)
            if cycle_flag==1:
                return
        elif visited_dict[i]==1 and i!=parent_dict[node]:
            cycle_flag=1
            return
        

g1 = Graph() 
g1.add_edge(1, 0) 
g1.add_edge(0, 2) 
g1.add_edge(0, 3) 
g1.add_edge(3, 4) 

g2 = Graph() 
g2.add_edge(1, 0) 
g2.add_edge(0, 2) 
g2.add_edge(2, 1) 
g2.add_edge(0, 3) 
g2.add_edge(3, 4) 

print(g1.d)
print(g2.d)

chkTree(g1)
chkTree(g2)
