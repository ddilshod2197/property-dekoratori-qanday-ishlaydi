class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Ismi string bolishi kerak")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Yosh 0 dan katta son bo'lishi kerak")
        self._age = value

    @age.deleter
    def age(self):
        del self._age

person = Person("Ali", 25)
print(person.name)  # Ali
print(person.age)   # 25

person.name = "Vali"
print(person.name)  # Vali

try:
    person.age = -10
except ValueError as e:
    print(e)  # Yosh 0 dan katta son bo'lishi kerak

try:
    person.name = 123
except TypeError as e:
    print(e)  # Ismi string bolishi kerak

del person.age
try:
    print(person.age)
except AttributeError as e:
    print(e)  # 'Person' object has no attribute 'age'
