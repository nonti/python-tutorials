class ArrayManager:
    def __init__(self):
        self.static_array = []
        self.dynamic_array = []
    def initialize_array(self,sample_list):
        self.static_array = sample_list
        
    def get_static_array(self):
        return self.static_array
    
    def initialize_dynamic_array(self, element):
        self.dynamic_array = element
        
    def append_to_dynamic_array(self, element):
        self.dynamic_array.append(element)
        
    def get_dynamic_array(self):
        return self.dynamic_array        
        
arr_manager = ArrayManager()
arr_manager.initialize_array([1,2,3,4,5])
print(arr_manager.get_static_array())
arr_manager.initialize_dynamic_array([1,2,3,4,5])
arr_manager.append_to_dynamic_array(6)
arr_manager.append_to_dynamic_array(7)
print(arr_manager.get_dynamic_array())