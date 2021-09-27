class Graph:

    def __init__(self):
        self.d = {}

    def add_node(self,name):
        self.d[name] = list()

    def add_edge(self,v1,v2):
        if v1 not in self.d.keys():
            self.add_node(v1)
        if v2 not in self.d.keys():
            self.add_node(v2)

        self.d[v1].append(v2)
        self.d[v2].append(v1)

    def chk_edge(self,v1,v2):
        if v1 not in self.d.keys() or v2 not in self.d.keys():
            return "NO"

        if v2 in self.d[v1]:
            return "YES"
        else:
            return "NO"


g = Graph()
n,m = [int(i) for i in input().split()]
for i in range(0,m):
    v1,v2 = [j for j in input().split()]
    g.add_edge(v1,v2)

q = int(input())
oplist = list()
for i in range(0,q):
    v1,v2 = [j for j in input().split()]
    oplist.append(g.chk_edge(v1,v2))

for i in range(q):
    print(oplist[i])