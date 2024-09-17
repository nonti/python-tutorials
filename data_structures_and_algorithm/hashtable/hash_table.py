class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for x in range(size)]
        
    def _hash(self,key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
        
    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        return None

hash_table = HashTable(3)
hash_table.insert('name', 'John')
hash_table.insert('age', 25)
print(hash_table.get('name'))  # Output: John
print(hash_table.get('age'))   # Output: 25
hash_table.delete('age')
print(hash_table.get('age'))   # Output: None
