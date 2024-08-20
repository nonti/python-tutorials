# List is and ordered mutable you can update the list
x = ['Python', 52.3, 'Zoe', 30]
y = x[2]
print(y)


print(len(x))
x.insert(2,'Kim')
print(x)

# Remove
x.remove('Zoe')
print(x)


# Clear 
x.clear()
print(x)

# #delete
# del x
# print(x)

# sort
b = [5,8,1,5,6,2,5,78,20]
b.sort()
print(b)
b.reverse()
print(b)
b.append(50)
print(b)


print(b.count(5))