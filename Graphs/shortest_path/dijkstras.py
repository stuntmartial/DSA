parent_dict={}
val_dict={}
class minheap:
    def __init__(self,arr):
        self.h=arr
        self.length=len(self.h)
        self.heapify()

    def heapify(self):
        print('Entered heapify...')
        if self.length==0:
            print('No nodes')
            return

        n=self.length-1
        for i in range(n-1,-1,-1):
            print(self.h)
            j=i

            while True:
                k=2*j+1
                l=2*j+2
                print(j,k,l)
                if k<self.length and l<self.length:
                    min_val=min(val_dict[self.h[j]],val_dict[self.h[k]],val_dict[self.h[l]])
                    
                    if min_val==val_dict[self.h[j]]:
                        break

                    elif min_val==val_dict[self.h[k]]:
                        self.h[j],self.h[k]=self.h[k],self.h[j]
                        j=k
                        continue

                    elif min_val==val_dict[self.h[l]]:
                        self.h[j],self.h[l]=self.h[l],self.h[j]
                        j=l
                        continue

                elif k<self.length:
                    min_val=min(val_dict[self.h[j]],val_dict[self.h[k]])

                    if min_val==val_dict[self.h[j]]:
                        break

                    elif min_val==val_dict[self.h[k]]:
                        self.h[j],self.h[k]=self.h[k],self.h[j]
                        j=k
                        continue

                elif l<self.length:
                    min_val=min(val_dict[self.h[j]],val_dict[self.h[l]])

                    if min_val==val_dict[self.h[j]]:
                        break

                    elif min_val==val_dict[self.h[l]]:
                        self.h[j],self.h[l]=self.h[l],self.h[j]
                        j=k
                        continue
                    
                else:
                    break

        print('leaving heapify')
        print(self.h)

    def delete(self,g):
        global parent_dict
        global val_dict
        print('heap ins del------>',self.h)
        print(self.length)
        t = self.h[0]
        self.h[0] = self.h[self.length - 1]
        self.length -= 1    
        i = 0
        for k in g.d[t]:
            if k in self.h[0:self.length]:
                if val_dict[k]>val_dict[t]+g.weights[str(t)+str(k)]:
                    val_dict[k]=val_dict[t]+g.weights[str(t)+str(k)]
                    parent_dict[k]=t

		
        while True:

            j = i*2 + 1
            k = i*2 + 2
		
            if j <= self.length and k <=self.length:

                min_val = min(val_dict[self.h[i]],val_dict[self.h[j]],val_dict[self.h[k]])

                if val_dict[self.h[i]] == min_val:
                    break

                elif val_dict[self.h[j]] == min_val:
                    self.h[j],self.h[i]=self.h[i],self.h[j]
                    i=j
                    continue

                elif val_dict[self.h[k]] == min_val:
                    self.h[k],self.h[i]=self.h[i],self.h[k]
                    i = k
                    continue

            elif j<=self.length:

                min_val = min(val_dict[self.h[i]],val_dict[self.h[j]])

                if val_dict[self.h[i]] == min_val:
                    break

                elif val_dict[self.h[j]] == min_val:
                    self.h[j],self.h[i] == self.h[i],self.h[j]
                    i = j
                    continue

            elif k<=self.length:

                min_val = min(val_dict[self.h[i]],val_dict[self.h[k]])

                if val_dict[self.h[i]] == min_val:
                    break

                elif val_dict[self.h[k]] == min_val:
                    self.h[k],self.h[i]=self.h[i],self.h[k]
                    i = k
                    continue

            else:
                break

        return t
    

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
        self.d[node2].append(node1)
        key1=str(node1)+str(node2)
        key2=str(node2)+str(node1)
        self.weights[key1]=weight
        self.weights[key2]=weight

        self.edges+=1

    def dijkistra(self,starting_node):
        global parent_dict
        global val_dict
        if starting_node not in self.d.keys():
            print('No such node')
            return 

        parent_dict={i:i for i in self.d.keys()}
        val_dict={}
        for i in self.d.keys():
            if i==starting_node:
                val_dict[i]=0
                continue
            val_dict[i]=1000000

        mh=minheap([i for i in self.d.keys()])
        print('heap---->',mh.h)
        op=[]
        while mh.length>0:
            
            node=mh.delete(self)
            print('node deleted---->',node)
            op.append(node)
            
            print(parent_dict)
            print(val_dict)

                    

        print(op)
        print(parent_dict)
        print(val_dict)



g=Graph()
g.add_edge('A','B',10)
g.add_edge('A','C',20)
g.add_edge('B','C',30)
g.add_edge('B','D',5)
g.add_edge('C','D',15)
g.add_edge('C','E',6)
g.add_edge('D','E',8)

print(g.d)
print(g.weights)

g.dijkistra(list(g.d.keys())[0])

g2=Graph()
g2.add_edge('A','B',5)
g2.add_edge('B','C',5)
g2.add_edge('C','D',2)
g2.add_edge('A','D',9)

g2.dijkistra(list(g2.d.keys())[0])