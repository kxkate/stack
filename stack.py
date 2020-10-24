class EmptyStackError(Exception):
    pass


class NotEnoughElements(Exception):
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

    def multi_pop(self, n):
        if len(self._data) < n:
            raise NotEnoughElements
        return [self.pop() for _ in range(n)]

        #zwraca liste n ostatnich elementow ze stacku
        #jesli elementow mniej niz n, to wyjątek ("Not enough elements to return"

    def pop(self):
        if not self._data:
            raise EmptyStackError
        return self._data.pop()

    def clear(self):
        self._data.clear()