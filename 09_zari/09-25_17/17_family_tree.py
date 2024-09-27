class Person:
    def __init__(self, name: str, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def get_parents(self):
        return self.mother, self.father
       
john = Person('John')
lena = Person('Lena')

peter = Person('Peter', mother=lena, father=john)

print(peter.get_parents()[0].name, peter.get_parents()[1].name) 
print(lena.get_parents())  


