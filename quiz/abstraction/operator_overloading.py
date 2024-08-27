# Python Operator Overloading Challenge

# 1. Create a ComplexNumber class:
class ComplexNumber(object):
    def __init__(self, real:0, imag:0):
        self.real = real
        self.imag = imag
    
# 2. In the '__add__' method:       
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            new_real = self.real + other.real
            new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

# 3. In the '__mul__' method:
    def __mul__(self, other):
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real *  other.imag + self.imag * other.real
        return ComplexNumber(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

# 4. In the '__str__' method:
    def __str__(self):
        return f'{self.real} + {self.imag}i'
        # return '%g + %gi' % (self.real, self.imag)
        # return "{0}+{1}i".format(self.real, self.imag)

# 5. Outside the class:
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1,2)
sum_result = num1 + num2 
product_result = num1 * num2

print('Sum: ', sum_result)
print('Product: ',product_result)
