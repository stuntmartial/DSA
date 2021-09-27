index=0
def find_depth(tree):
    global index
    if tree[index]=='l':
        return

    ht=func(tree)
    print('height is : ',ht)

def func(tree):
    global index

    if tree[index]=='l' or index==len(tree):
        return 0

    index+=1
    lht=func(tree)
    index+=1
    rht=func(tree)

    ht=1+max(lht,rht)
    return ht

tree="nlnnlll"
find_depth(tree)