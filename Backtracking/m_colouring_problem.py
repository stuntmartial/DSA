class graph:
    def __init__(self):
        self.d={}
        self.nodes=0
        self.edges=0
        self.ini_node=None
        
    def add_node(self,node):
        if node not in self.d.keys():
            self.d[node]=[]
            if self.nodes==0:
                self.ini_node=node
                
            self.nodes+=1
            
    def add_edge(self,node1,node2):
        if node1 not in self.d.keys():
            self.add_node(node1)
        if node2 not in self.d.keys():
            self.add_node(node2)
            
        if node2 in self.d[node1]:
            return
        self.d[node1].append(node2)
        self.d[node2].append(node1)
        self.edges+=1
        
    def mcolor(self,m):
        #print(self.d)
        q=[self.ini_node]
        q_color_dict={self.ini_node:1}
        visited_dict={self.ini_node:1}
        for i in list(self.d.keys()):
            if i!=self.ini_node:
                q_color_dict[i]=0
                visited_dict[i]=0
        
        flag=0
        while(len(q)>0):
            v=q.pop(0)
            if v==None:
                break
            for i in self.d[v]:
                if visited_dict[i]==0:
                    q.append(i)
                    visited_dict[i]=1
                
                col_dict={i:i for i in range(1,m+1)}
                for j in self.d[i]:
                    if q_color_dict[j]!=0:
                        try:
                            col_dict.pop(q_color_dict[j])
                        except:
                            pass
                if len(list(col_dict.keys()))==0:
                    flag=1
                    break
                
                q_color_dict[i]=list(col_dict.keys())[0]
                
            if flag==1:
                break
            
        if flag==1:
            return 0
        elif flag==0:
            return 1
            
oplist=[]
T=int(input())
for i in range(T):
    v=int(input())
    m=int(input())
    e=int(input())
    eli=[j for j in input().split()]
    
    g=graph()
    j=0
    while j<2*e:
        g.add_edge(eli[j],eli[j+1])
        j=j+2
        
        
    flag=g.mcolor(m)
    oplist.append(flag)
    
for i in oplist:
    print(i)
