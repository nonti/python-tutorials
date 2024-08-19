cls_room = { 'name':'Kim','age':20 }
print(cls_room['name'])
print(cls_room['age'])

emp = { 'name':'Kim','age':24, 'smoke':False, ('h', 'w'):(6,78)}
print(emp['name'])
print(emp['age'])
print(emp['smoke'])
print(emp[('h', 'w')])

#add a value
emp['city'] = 'Seoul'
print(emp)
print(len(emp))

# get a key or value
print(emp.get('city'))

#pop to remove the last value
print(emp.pop('city'))
print(emp)

# delete 
# del emp['smoke']
# print(emp)

# to get values
print(emp.values())

print(emp.items())
 
#to update 
emp['age'] = 25
print(emp.items())
