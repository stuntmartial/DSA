list_of_cycles=[]
count=0
class Graph:
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
        self.edges+=1

    def finc_cycle_length_n(self,n):
        global count
        V=len(self.d.keys())
        print(V)
        if n>V:
            print('None')
            return

        no=V-(n-1)
        for i in range(no):
            vertex=list(self.d.keys())[i]
            visited_dict={i:0 for i in self.d.keys()}
            visited_dict[vertex]=1
            curr=0
            curr_vertex=vertex
            print('curr-->',curr_vertex)
            self.find_cycle_helper(vertex,n,curr,curr_vertex,visited_dict,str(curr_vertex))

        print(count)

    def find_cycle_helper(self,vertex,n,curr,curr_vertex,visited_dict,s):
        global list_of_cycles
        global count
        print('curr_vertex--->',curr_vertex)
        print(visited_dict)
        if curr==n-1:
            if vertex in self.d[curr_vertex] and chk_duplicate(s)==False:
                count+=1
                print(s,count)
                list_of_cycles.append(s)
            return
        
        for i in self.d[curr_vertex]:
            if visited_dict[i]==0:
                visited_dict[i]=1
                curr+=1
                s=s+str(i)
                self.find_cycle_helper(vertex,n,curr,i,visited_dict,s)
                visited_dict[i]=0
                curr-=1
                s=s[0:len(s)-1]

def chk_duplicate(s):
    global list_of_cycles
    print('mmmmmmmmmmmmmmm',list_of_cycles,s)
    for i in list_of_cycles:
        flag=0
        for j in s:
            if j in i:
                flag+=1
        if flag==len(i):
            return True 
        else:
            continue

    return False

'''
list_of_cycles=['abc','cde']
print(chk_duplicate('edc'))
'''

g=Graph()
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,4)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)

g.finc_cycle_length_n(4)
