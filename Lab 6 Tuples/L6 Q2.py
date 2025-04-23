import operator
l=[(1,'abcd',18),(2,'efgh',18),(3,'ijkl',17),(4,'mnop',18)]
l1=[]
l2=[]
l3=[]
for i in l :
        l1.append(i[0])
        l2.append(i[1])
        l3.append(i[2])
print(l1,l2,l3,sep=" ***** ")
