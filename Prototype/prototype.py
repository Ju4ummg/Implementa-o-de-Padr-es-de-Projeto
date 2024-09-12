import copy

class Prototype:
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f'{self.name}: {self.data}'

# Uso do padrão Prototype
obj1 = ConcretePrototype("Objeto 1", {"key": "value"})
obj2 = obj1.clone()

print(obj1)  # Saída: Objeto 1: {'key': 'value'}
print(obj2)  # Saída: Objeto 1: {'key': 'value'}