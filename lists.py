a=[1,2,3,4,4,8,5,6] #list
b=[1,2,3,4,5,5,6]
#list(a) #creating a list
print(list(a)) #printing a list
print(a[1]) #accessing elements
print(a[1:4]) #accessing range of elements(last is not included)
a[1]=90 #changing element in list
a.insert(4,78) #using insert function
list.extend(a,b)
list.append(a,33) 
print(list(a))