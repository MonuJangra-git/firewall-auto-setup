import itertools
list1 = [1,2,9,7,6]
listn=[str(i) for i in list1]
with open("paswd.txt","w") as f:
    list2=listn
    for i in range(1,len(list2)):
        perm = list(itertools.product(list2,repeat=i))
        for j in perm:
            joint = ''.join(j)
            f.write(joint+"\n")