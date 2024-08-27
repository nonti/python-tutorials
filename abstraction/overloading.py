a = 10
b = 20

# Addition
print(a + b)

p = 'Hello'
q = 'World'
print(p + q)

x = [12, 20, 30]
y = [5,6,7]
print(x + y)


class Books:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages
    
    def __mul__(self, other):
        return self.pages * other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages

b1 = Books(100)
b2 = Books(200)

print(b1 + b2) #b1.__add__(b2)
print(b1 * b2) #b1.__mul__(b2)
print(b1 > b2) #b1.__gt__(b2)