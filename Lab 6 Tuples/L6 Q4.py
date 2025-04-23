import operator 
l=[('kurkure',20),('popcorn',200),('wafer',50),('good day',40)]
print(sorted(l,key=operator.itemgetter(1)))
