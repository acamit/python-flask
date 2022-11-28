class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id = {self.id} ---- name = {self.name}'

class PersonFactory:
    Count = 0

    def create_person(self, name):
        p = Person(PersonFactory.Count, name)
        PersonFactory.Count = PersonFactory.Count + 1
        return p
pf = PersonFactory()

p1 = pf.create_person("Amit")
print(p1)


p2 = pf.create_person("Sumit")
print(p2)


p2 = pf.create_person("Sumit")
print(p2)