#Инкапсуляция
class BankAccount:
    def __init__(self, user_name,balance,pin_code):
        self.user_name = user_name
        #protected
        self._balance = balance
        #privete
        self.__pin_code = pin_code

    def take_balance(self):
        return self._balance

John = BankAccount("John",100000,"123456")
print(John.user_name)
print(John.take_balance())
print(dir(John))
print(John._BankAccount__pin_code)


from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        # ...
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Gaf gaf")

    def move(self):
        print("step")

class Cat(Animal):

    def make_sound(self):
        print("myu myu")

    def move(self):
        print("step")

gufi = Dog()
