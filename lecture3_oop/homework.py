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
        self.availability_of_money += random.randint(400, 1000)
        print(f'Looking for house up to {self.availability_of_money}$.')

    def person_buy_a_house(self, house):
        if self.having_your_own_home is True and self.availability_of_money >= house.house_cost:
            print(f'{self.name} has the house, but want to buy house "{house.house_name}".')
        elif self.availability_of_money >= house.house_cost:
            print(f'{self.name} want to buy house "{house.house_name}".')
        else:
            print(f'{self.name} have no money for house "{house.house_name}".')


class House:
    def __init__(self, house_name, house_area, house_cost, house_discount):
        self.house_name = house_name
        self.house_area = house_area
        self.house_cost = house_cost
        self.house_discount = house_discount

    def house_info(self):
        print(f'- House "{self.house_name}" with {self.house_area} square meters cost {self.house_cost}$.')

    def discount_for_house(self):
        self.house_cost = int(self.house_cost - self.house_cost * self.house_discount / 100)
        print(f'  For house "{self.house_name}" can be discount {self.house_discount}%.\n'
              f'  Price with discount will be {self.house_cost}%!')


class SmallHouse(House):
    def __init__(self, house_name, house_area, house_cost, house_discount):
        super().__init__(house_name, house_area, house_cost, house_discount)

    def small_house_info(self):
        print(
            f'-- There is also a small house "{self.house_name}" '
            f'   with a required area of {self.house_area} square meters')

    def small_house_discount(self):
        self.house_cost = int(self.house_cost - self.house_cost * self.house_discount / 100)
        print(f'   Discount can be only {self.house_discount}%.\n'
              f'   Price with discount {self.house_cost}$!')


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, realtor_discount):
        self.name = name
        self.realtor_discount = realtor_discount

    def info(self):
        print(f'Hello, my name is {self.name}, I will help you to find house of your dream:')

    def discount(self, house):
        house.house_cost = int(house.house_cost - house.house_cost * self.realtor_discount / 100)
        print(f'- You can get plus my {self.realtor_discount}% discount:\n'
              f'- Price for house {house.house_name} will be {house.house_cost}$!')

    def steal_money(self, human, house):
        if random.randint(1, 10) == 1 and human.availability_of_money >= house.house_cost:
            human.availability_of_money = 0
            print(f'Realtor {self.name} had stolen {human.name}`s money!!!\n'
                  f'Now {human.name} have {human.availability_of_money}$.')
        elif human.availability_of_money < house.house_cost:
            pass
        else:
            print(f'Congrats with buying new home. {self.name} - good realtor!')


realtor = Realtor('Ann', 10)

realtor.info()

house1 = House('Dream', 100, 55000, 5)
house2 = House('Sky', 150, 75000, 7)
house3 = House('Ocean', 200, 90000, 8)
small_house = SmallHouse('Hunting Lodge', 40, 30000, 3)

house1.house_info()
house1.discount_for_house()
house2.house_info()
house2.discount_for_house()
house3.house_info()
house3.discount_for_house()
small_house.small_house_info()
small_house.small_house_discount()
print('------------------------------------------------')
tom = Human('Tom', 25, 40000, True)
tom.person_info()
tom.person_make_money()
realtor.discount(house1)
tom.person_buy_a_house(house1)
realtor.steal_money(tom, house1)
print('------------------------------------------------')
john = Human('John', 28, 52000, False)
john.person_info()
john.person_make_money()
realtor.discount(house1)
john.person_buy_a_house(house1)
realtor.steal_money(john, house1)

print('------------------------------------------------')
kate = Human('Kate', 30, 100000, True)
kate.person_info()
kate.person_make_money()
realtor.discount(house3)
kate.person_buy_a_house(house3)
realtor.steal_money(kate, house3)

print('------------------------------------------------')
kim = Human('Kim', 22, 30000, False)
kim.person_info()
kate.person_make_money()
realtor.discount(small_house)
kim.person_buy_a_house(small_house)
realtor.steal_money(kate, small_house)
