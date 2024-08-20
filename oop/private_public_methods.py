class Example:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 100
        
    def public_method(self):
        print('Public method', self.x)
        print('Public method', self._y)
        print('Private method', self.__z)
        self.__private_method()
        
    def __private_method(self):
        print('Inside a private method')

s  = Example()
s.public_method()
# s.__private_method()