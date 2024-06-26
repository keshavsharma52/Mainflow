dict1={
    "name": "swastik",
    "roll no" : "316",
    "department": "cse" }
print((dict1))
print(dict['name']) #printing specific value using key
x= dict1.get('roll no') #using get method
print(x)
y= dict1.keys() #printing all keys
print(y)
dict1['course']='BTech' #adding new key and value
print(dict1)
z= dict1.values() #printing all values
print(z)
if 'name' in dict1:   #checking for keys in dictionary
    print('Yes, name is on of the keys')
dict1.update({'name':'rohit'})  #changing values in dictionary
print(dict1)
del dict1['department'] #deleting key
print(dict1)
dict2={ #nested dictionary
    "name": "rohit",
    "roll no" : "318",
    "department": "cse" }
dict3={
    "name": "keshav",
    "roll no" : "299",
    "department": "me" }
dict4={
   "name": "lakshay",
    "roll no" : "313",
    "department": "eee" }
students = {
  'dict1' : dict1,
  'dict2' : dict2,
  'dict3' : dict3,
  'dict4' : dict4
}
print(students)





