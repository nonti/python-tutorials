x = 'hello world'
y = 'HELO WORLD'
a = 'hello, world'

print(x.capitalize())
print(y.capitalize())

print(x.upper())
print(y.lower())

# indexing 
print(x[0])
print(y[6])

# substring slicing
print(x[0:5])
print(y[0:2])

z = '      Hello World    '
print(z.strip(), "Strip")
print(z.lstrip(), "L strip")
print(z.rstrip(), "R strip")

#  replace 
print(x.replace('l', 'L'))
print(y.replace('WORLD', 'mE'))

print(a.split(','))