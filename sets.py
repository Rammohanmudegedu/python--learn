set1={1,3,5,7,8,9}
set2={2,3,4,8,9,10,13,17}
set1.add(6)
set2.update([1,5,"ram","mohan"])
set2.discard("mohan")
set2.remove("ram")
set2.clear()
print(set1)
print(set2)

#methematical methods

set3={2,10,5,4,6}
set4={3,7,4,5,2,6,9}

#print(set3.union(set4))
print(set3|set4)
#print(set3.intersection(set4))
print(set3 & set4)
#print(set3.difference(set4))
print(set3-set4)
#print(set4.difference(set3))
print(set4-set3)
#print(set3.symmetric_difference(set4))
print(set3^set4)
print(sum(set3))
print(sorted(set4))
print(len(set3))