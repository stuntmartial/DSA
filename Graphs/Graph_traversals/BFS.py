class Graph:

    def __init__(self):
        self.d = {}
        self.nodes = 0
        self.edges = 0

    def add_node(self,name):
        self.d[name] = list()
        self.nodes += 1
        print("Node added")

    def add_edge(self,v1,v2):
        if v1 not in self.d.keys():
            self.add_node(v1)
        if v2 not in self.d.keys():
            self.add_node(v2)

        self.d[v1].append(v2)
        self.d[v2].append(v1)

        print("Egde added")

        self.edges += 1

    def bfs(self,starting_node):


        if self.edges == 0:
            print("No egdes")
            return 

        print(self.edges)
        q = list()
        q.append(starting_node)
        binary_hash_table = {}
        binary_hash_table.update({starting_node:1})
        for i in self.d.keys():
            if starting_node != i:
                binary_hash_table.update({i:0})

        while(len(q)!=0):
            v = q.pop(0)

            for i in self.d[v]:

                if binary_hash_table[i] == 0:
                    q.append(i)
                    binary_hash_table[i] = 1

            print(v)

g = Graph()
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(input())
    elif x == 2:
        g.add_edge(input(),input())
    elif x == 3 :
        g.bfs("v1")
    else:
        print("Terminating...")
        break
