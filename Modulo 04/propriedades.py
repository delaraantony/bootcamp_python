#Exemplo de codigo com uso de propriedades
# class Foo

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, valor):
        _x = self._x or 0
        _value = valor or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)  # Saída: 10
foo.x = 5
print(foo.x)  # Saída: 15
del foo.x
print(foo.x)  # Saída: -1