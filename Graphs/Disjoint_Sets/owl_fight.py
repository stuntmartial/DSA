class Disjoint_Set:
    def __init__(self,arr):
        self.arr=arr
        self.parent={i:i for i in self.arr}

    def find_path_compress(self,ele):
        if ele==self.parent[ele]:
            print(ele)
            return self.parent[ele]

        par=self.find_path_compress(self.parent[ele])
        self.parent[ele]=par
        return par

    def union_byVal(self,ele1,ele2):
        parent_ele1=self.find_path_compress(ele1)
        parent_ele2=self.find_path_compress(ele2)

        if parent_ele1==parent_ele2:
            return

        elif parent_ele1>parent_ele2:
            self.parent[parent_ele2]=parent_ele1
            return

        elif parent_ele2>parent_ele1:
            self.parent[parent_ele1]=parent_ele2
            return

    def find_winner(self,ele1,ele2):
        parent_ele1=self.find_path_compress(ele1)
        parent_ele2=self.find_path_compress(ele2)

        if parent_ele1==parent_ele2:
            print("Draw...")
            return
        
        elif parent_ele1>parent_ele2:
            print(ele1," wins...")

        elif parent_ele2>parent_ele1:
            print(ele2,' wins...')

ds=Disjoint_Set([1,2,3,4,5,6,7])
while True:
    ch=int(input("Enter choice : "))

    if ch==1:
        ds.find_path_compress(int(input("Enter ele : ")))

    elif ch==2:
        ds.union_byVal(int(input('Enter ele1 : ')),int(input('Enter ele2 : ')))

    elif ch==3:
        print(ds.parent)

    elif ch==4:
        ds.find_winner(int(input('Enter ele1 : ')),int(input('Enter ele2 : ')))

    else:
        print('Terminating...')
        break