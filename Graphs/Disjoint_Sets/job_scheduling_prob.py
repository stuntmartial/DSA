class Disjoint_Set:
    def __init__(self,arr):
        self.arr=[-1]*len(arr)
        self.parent={i:i for i in arr}

    def find_path_comp(self,ele):
        if self.parent[ele]==ele:
            return ele

        par=self.find_path_comp(self.parent[ele])
        self.parent[ele]=par
        return par        

    def union(self,ele1,ele2):
        self.parent[ele2]=ele1

def job_seq(job_ids,deadlines,profits_dict):
    max_d=max(deadlines)
    dj=Disjoint_Set(range(max_d+1))
    profits_list=[i for i in profits_dict.keys()]
    profits_list.sort(reverse=True)
    print(profits_list)

    for i in profits_list:
        
        job_id=profits_dict[i]
        print('job_id---->',job_id)
        for j in range(len(job_ids)):
            if job_ids[j]==job_id:
                break

        deadline=deadlines[j]
        print('Deadline---->',deadline)
        time_slot=dj.find_path_comp(deadline)
        print('Time_slot---->',time_slot)
        if time_slot>0:
            dj.arr[time_slot-1]=job_id
            dj.union(dj.find_path_comp(time_slot-1),dj.find_path_comp(time_slot))
            print(job_id)

    print(dj.arr)

job_ids=['a','b','c','d','e']
deadlines=[2,1,2,1,3]
profits_dict={100:'a',19:'b',27:'c',25:'d',15:'e'}
job_seq(job_ids,deadlines,profits_dict)

job_ids2=['a','b','c','d']
deadlines2=[4,1,1,1]
profits_dict2={10:'a',20:'b',40:'c',30:'d'}
job_seq(job_ids2,deadlines2,profits_dict2)
