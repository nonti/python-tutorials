# +----+---+---+---+---+-------
# |P|y|t|h|o|n|
# +----+---+---+----+----+---+----+
# 0, 1, 2,3,4,5
#-6,-5,-4,-3,-2,-1

x = [100,101,102,103,104,105,106,107,108,109]
y = (00,10,20,30,40,50,60,70,80,90)
z = 'python'

# indexing to fetch a value using a positive and negative 
# start: 0 end: 3 gap: 1
i = x[0:3:1]
print(i)

#print the last element from the array
k = x[4:]
print(k)

# print the first 5 element
l = x[:5]
print(l)

# print all the values
print(x[:])

#get gap of 2
print(x[::2])

# negative indexing output in reverse order
print(x[::-1])

print(z[::-1])
print(z[-2::])

# search a value
print(z[4:0:-1], 'Search a value')