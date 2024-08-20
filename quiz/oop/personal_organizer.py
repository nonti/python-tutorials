# Personal Details Organizer

#1. Define Person class with name, age, and city attributes
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    #2. Initialize Person object with provided name, age, and city
    def display_info(self):
        print('Name:', self.name, ',Age:', self.age, ',City:', self.city)
    #3. Display person's information

#4. Create Person instance with specific values
p1 = Person('John Doe', 25, 'New York')
#5. Print person's information using display_info method
p1.display_info()