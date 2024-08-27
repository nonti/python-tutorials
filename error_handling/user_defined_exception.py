class TeaHotException(Exception):
    def __init__(self,arg):
        self.msg = arg

class TeaColdException(Exception):
    def __init__(self,arg):
        self.msg = arg
class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature
        
    def drink_tea(self):
        if self.__temperature > 85:
            raise TeaHotException('Tea to hot') # whenever you want it can be raised
        elif self.__temperature < 65:
            raise TeaColdException('Tea too Cold to drink')
        else:
            print('Tea OK to Drink')
            
cup = Tea(89)
cup.drink_tea()
            