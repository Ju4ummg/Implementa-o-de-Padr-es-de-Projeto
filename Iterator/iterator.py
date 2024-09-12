from collections.abc import Iterator, Iterable

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
        except IndexError:
            raise StopIteration()
        self._position += 1
        return value


class ConcreteAggregate(Iterable):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return ConcreteIterator(self._items)


# Uso do Iterator
collection = ConcreteAggregate()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

print("Iterando sobre a coleção:")
for item in collection:
    print(item)