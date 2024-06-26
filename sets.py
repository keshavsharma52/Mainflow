c={1,2,3,4,4,8,95,6} #set
d={'a','b','c','d','e','f'}
set(c) creating a set
print(set(c))
print(3 in c)
c.add(33) adding element
c.remove(4) removing element
print(set(c))
c.update(d) #adding two sets
print(c)
c.remove(2) #removing element
c.clear() #delete all data from set
del c #delete whole set
print(c)