# Implementação de Padrões de projeto

## Padrão Prototype:
O que é o Prototype? O padrão Prototype é utilizado para criar novos objetos copiando ou "clonando" objetos existentes, sem depender da classe concreta desses objetos. Ele é útil quando o custo de criar um objeto diretamente é caro ou quando você quer evitar repetições de código ao criar múltiplos objetos similares.

Problema que resolve: Ele resolve o problema de criação de objetos de maneira eficiente, especialmente quando o processo de criação é custoso ou envolve várias configurações de estado. Um exemplo clássico é a criação de um objeto que possui configurações internas complexas ou que precisa ser duplicado várias vezes com pequenas alterações.

Solução: O padrão define uma interface de clonagem que permite criar uma cópia do objeto atual, sem depender de seu tipo concreto. Isso permite clonar objetos sem precisar conhecer a classe exata do objeto que está sendo clonado.

### Exemplificando prototype do código
```python
    class Prototype:
    def clone(self):
        pass
```
A classe Prototype define a interface de clonagem

```python
    class ConcretePrototype(Prototype):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f'{self.name}: {self.data}'
```
A classe ConcretePrototype implementa o método clone(), que usa a função deepcopy para criar uma cópia profunda do objeto

```python
    obj1 = ConcretePrototype("Objeto 1", {"key": "value"})
    obj2 = obj1.clone()
```
O objeto obj1 é criado e depois clonado para obj2. Ambos os objetos possuem o mesmo conteúdo, mas são instâncias diferentes.

