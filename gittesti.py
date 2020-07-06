class Person:

    def __init__(self, name, age, city, address, phone_number, pet):
        self._name = name
        self._age = age
        self._city = city
        self._address = address
        self._phone_number = phone_number
        self.pet = pet

    def flexaa(self):
        return f'{self.name} sanoo 1+1 = 2'
