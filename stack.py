class EmptyStackError(Exception):
    pass
class Stack:
    def __init__(self):
        self._data = []

    @property  #  zmienia zachowaniu funkcji albo metody nie zmieniajac metody, nie zmienia funkjonalnosci
    def size(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def peek(self):
        return self._data[-1]

    def pop(self):
        if not self._data:
            raise EmptyStackError
        return self._data.pop()

    def clear(self):
        self._data.clear()