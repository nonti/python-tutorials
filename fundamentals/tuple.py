# a sequence of immutable objects, are like lists with the exception that tuples canot be changed once declared,
a  = (10, 15, 20, 25, 50)
print(a[0])
print(a.count(25))

b = (10, 15, 10, 'Kim', 5.5, [10, 5])
print(b.count(10))
print(len(b)) 
# concatenation
c = (23, 89, 80)
e = (34, 55)
d = c + e
print(d)
a = d
print(a)
print(max(a,))
p = ('Hello', ) * 5 # this means its a tuple for single element
print(p)