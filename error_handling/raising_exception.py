class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature
        
    def drink_tea(self):
        if self.__temperature > 85:
            raise Exception('Tea to hot') # whenever you want it can be raised
        elif self.__temperature < 65:
            print('Cold to drink')
        else:
            print('Tea OK to Drink')
            
cup = Tea(1100)
cup.drink_tea()
            