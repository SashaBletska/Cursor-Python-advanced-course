from abc import ABC, abstractmethod
import random


class Person(ABC):
    def __init__(self, name, age, availability_of_money, having_your_own_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_your_own_home = having_your_own_home

    @abstractmethod
    def person_info(self):
        raise NotImplementedError('This method is not realised')

    @abstractmethod
    def person_make_money(self):
        raise NotImplementedError('This method is not realised')

    @abstractmethod
    def person_buy_a_house(self, house):
        raise NotImplementedError('This method is not realised')


class Human(Person, ABC):
    def __init__(self, name, age, availability_of_money, having_your_own_home):
        super().__init__(name, age, availability_of_money, having_your_own_home)

    def person_info(self):
        print(f'Buyer name: {self.name}.\n'
              f'Buyer age: {self.age}.')

    def person_make_money(self):
        self.availability_of_money += 1000
        print(f'Looking for house up to {self.availability_of_money}$.')

    def person_buy_a_house(self, house):
        if self.having_your_own_home is True and self.availability_of_money >= house.house_cost:
            print(f'{self.name} has the house, but want to buy house "{house.house_name}".')
        elif self.availability_of_money >= house.house_cost:
            print(f'{self.name} want to buy house "{house.house_name}".')
        else:
            print(f'{self.name} have no money for house "{house.house_name}".')


class House:
    def __init__(self, house_name, house_area, house_cost):
        self.house_name = house_name
        self.house_area = house_area
        self.house_cost = house_cost

    def house_info(self):
        print(f'- House "{self.house_name}" with {self.house_area} square meters cost {self.house_cost}$.')


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount_for_house):
        self.name = name
        self.discount_for_house = discount_for_house

    def info(self):
        print(f'Hello, my name is {self.name}, I will help you to find house of your dream:')

    def discount(self):
        print(f'You can get {self.discount_for_house}% discount.')

    def steal_money(self, human, house):
        if random.randint(1, 10) == 1 and human.availability_of_money >= house.house_cost:
            print(f'Realtor {self.name} had stolen {human.name} money!!!')
        elif human.availability_of_money < house.house_cost:
            pass
        else:
            print(f'Congrats with buying new home. {self.name} - good realtor!')


realtor = Realtor('Ann', 10)

realtor.info()

house1 = House('Dream', 100, 55000)
house2 = House('Sky', 150, 75000)
house3 = House('Ocean', 200, 90000)

house1.house_info()
house2.house_info()
house3.house_info()

realtor.discount()
print('------------------------------------------------')
tom = Human('Tom', 25, 50000, True)
tom.person_info()
tom.person_make_money()
tom.person_buy_a_house(house1)
realtor.steal_money(tom, house1)
print('------------------------------------------------')
john = Human('John', 28, 70000, False)
john.person_info()
john.person_make_money()
john.person_buy_a_house(house1)
realtor.steal_money(john, house1)

print('------------------------------------------------')
kate = Human('Kate', 30, 100000, True)
kate.person_info()
kate.person_make_money()
kate.person_buy_a_house(house3)
realtor.steal_money(kate, house3)

