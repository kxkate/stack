### BIBLIOTEKA UNITTEST #####
from unittest import TestCase
from stack import Stack, EmptyStackError, NotEnoughElements


class TestStackOperations(TestCase):
    def setUp(self):  #  uruchamiany przed każdym testem
        self.stack = Stack()  # w selfie atrybut o nazwie stack

    def tearDown(self):  #  sprzątanie po każdym teście
        self.stack.clear()

    def test_should_add_new_element_to_stack(self):  # najlepiej napisac, co powinno sie zadziac w tym tescie, a nie tylko test_push()
        value, expected = 42, 42
          #  sekcja 1 - tworzymy obiekt naszego stacka. Instancja klasy Stack

        self.stack.push(value)   #  sekcja 2 - wywołujemy nechanizm, który testujemy

        self.assertEqual(self.stack.peek(), expected)  #  sekcja 3 sprawdzamy, (co na szczycie stacku) czy mechanizm dziala tak, jak chcielismy
        #assert stack.peek() == 42  w klasie Test Case sa metody asercje
    def test_should_remove_last_element_from_stack(self):
        element, expected = 42, 42
        self.stack.push(element)

        value = self.stack.pop()

        self.assertEqual(value, expected)
        self.assertEqual(self.stack.size, 0)

    def test_peek_should_return_last_element_from_stack_and_not_remove_it(self):
        element, expected = 21, 21
        self.stack.push(element)  # stack._data.append(element), ale to zły znak, zeby sie odwolywac do enkapsulowanych danych
        # analogia z człowiekiem i jedzeniem
        value = self.stack.peek()

        self.assertEqual(value, expected)
        self.assertEqual(self.stack.size, 1)

    def test_should_return_stack_size(self):
        element = 21
        self.stack.push(element)
        value = self.stack.size

        self.assertEqual(self.stack.size, 1)

    def test_should_clear_stack(self):
        self.stack.push(42)
        self.stack.push(43)

        self.stack.clear()

        self.assertEqual(self.stack.size, 0)

    def test_should_raise_when_called_pop_on_empty_stack(self):
          # robimy zaślepkę. Test, który od razu failuje
        # self.fail("Not implemented yet")  # test przy uruchomieniu padnie
        self.assertRaises(EmptyStackError, self.stack.pop)

    def test_multipop_raises_if_numb_of_elements_is_less_than_in_stack(self):
        self.assertRaises(NotEnoughElements, self.stack.multi_pop, 2)
        #multipop rzuca wyjatek, gdy dlugosc stacku jest mniejsza niz n, funkcja multipop z parametrem 2


    def test_multipop_should_return_two_elements(self):
        expected = [9, 8, 7, 6]
        for elem in range(10):
            self.stack.push(elem)

        result = self.stack.multi_pop(4)

        self.assertEqual(result, expected)