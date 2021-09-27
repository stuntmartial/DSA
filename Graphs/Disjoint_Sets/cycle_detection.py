class Graph:
    def __init__(self):
        self.d=dict()
        self.nodes=0
        self.edges=0
        self.edge_list=list()

    def add_node(self,node):
        if node in self.d.keys():
            return

        self.d[node]=[]
        self.nodes+=1

    def add_edge(self,node1,node2):
        if node1 not in self.d.keys():
            self.add_node(node1)
        if node2 not in self.d.keys():
            self.add_node(node2)

        if node2 not in self.d[node1]:
            self.d[node1].append(node2)
        if node1 not in self.d[node2]:
            self.d[node2].append(node1)

        self.edge_list.append(str(node1)+str(node2))
        self.edges+=1

    def detect_cycle(self):
        nodes_arr=[i for i in self.d.keys()]
        print('nodes_arr--> ',nodes_arr)
        print('Edge_list-->',self.edge_list)
        djs=Disjoint_Set(nodes_arr)
        processed_edge_dict={i:0 for i in self.edge_list}
        for i in self.edge_list:
            if processed_edge_dict[i]==0:
                print('Workin on...',i)
                node1=int(i[0])
                node2=int(i[1])
                processed_edge_dict[str(node1)+str(node2)]=1
                processed_edge_dict[str(node2)+str(node1)]=1
                node1_parent=djs.find(node1)
                node2_parent=djs.find(node2)
                if node1_parent==node2_parent:
                    print('Cycle Detected')
                    return

                else:
                    djs.union(node1,node2)
                    print(djs.parent)

        print('No cycle...')
    
    def disp(self):
        if self.nodes==0:
            print('No nodes')
            return
        
        print(self.d)

class Disjoint_Set:
    def __init__(self,arr):
        self.parent={i:i for i in arr}
        self.rank={i:1 for i in arr}
        print(self.parent)

    def find(self,node):
        '''
        if node not in self.parent.keys():
            print('No such nodes...')
            return
        '''
        parent_node=self.find_path_cmp(node)
        print(parent_node)
        return parent_node

    def find_path_cmp(self,node):
        if self.parent[node]==node:
            return node

        self.parent[node]=self.find_path_cmp(self.parent[node])
        return self.parent[node]

    def union(self,node1,node2):
        parent_node1=self.find(node1)
        parent_node2=self.find(node2)
        if parent_node1==parent_node2:
            return

        if self.rank[parent_node1]==self.rank[parent_node2]:
            self.parent[parent_node1]=parent_node2
            self.rank[parent_node2]+=self.parent[parent_node1]

        elif self.rank[parent_node1]>self.rank[parent_node2]:
            self.parent[parent_node2]=parent_node1
            self.rank[parent_node1]+=parent_node2

        elif self.rank[parent_node2]>self.rank[parent_node1]:
            self.parent[parent_node1]=parent_node2
            self.rank[parent_node2]+=parent_node1

g=Graph()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)
#g.add_edge(5,1)
g.disp()
g.detect_cycle()