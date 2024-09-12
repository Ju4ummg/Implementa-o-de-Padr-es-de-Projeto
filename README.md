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
->A classe Prototype define a interface de clonagem

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
->A classe ConcretePrototype implementa o método clone(), que usa a função deepcopy para criar uma cópia profunda do objeto

```python
    obj1 = ConcretePrototype("Objeto 1", {"key": "value"})
    obj2 = obj1.clone()
```
->O objeto obj1 é criado e depois clonado para obj2. Ambos os objetos possuem o mesmo conteúdo, mas são instâncias diferentes.

## Padrão Adapter
O que é o Adapter? O Adapter é um padrão estrutural que permite que classes com interfaces incompatíveis trabalhem juntas. Ele funciona como um intermediário que converte a interface de uma classe para uma interface esperada por um cliente.

Problema que resolve: Muitas vezes, em sistemas complexos, você encontra classes já implementadas que não podem ser modificadas. Quando estas classes precisam se comunicar com outras que esperam uma interface diferente, o Adapter entra em cena para fazer a "conversão".

Solução: O Adapter cria uma interface de compatibilidade entre duas classes que não podem interagir diretamente devido a interfaces diferentes.

### Exemplificando adapter do código
```python
    class Target:
        def request(self):
            return "Target: The default target's behavior."
```
->A classe Target é a interface que o cliente espera

```python
    class Adaptee:
        def specific_request(self):
            return ".eetpadA eht fo roivaheb laicepS"
```
->Classe Adaptee é uma clase com uma interface incompatível

```python
    class Adapter(Target):
        def __init__(self, adaptee: Adaptee):
            self.adaptee = adaptee

        def request(self):
            return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
```
->A classe Adapter adapta a interface do Adaptee para ser uma interface compatível com Target,traduzindo a chamada do método specific_request() para o método request(). 
