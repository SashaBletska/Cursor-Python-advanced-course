"""1. Create a class hierarchy of animals with at least 5 animals that have additional methods
each, create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class"""


class Animal:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def print_animal_info(self):
        print(f"My name is {self.name}. I like to eat {self.eat}. I sleep all the {self.sleep}.")


class Dog(Animal):
    def __init__(self, name, eat, sleep, does):
        super().__init__(name, eat, sleep)
        self.does = does

    def print_dog_does(self):
        print(f"I am {self.does}.")


class Cat(Animal):
    def __init__(self, name, eat, sleep, does):
        super().__init__(name, eat, sleep)
        self.does = does

    def print_cat_does(self):
        print(f"I am {self.does}.")


class Rabbit(Animal):
    def __init__(self, name, eat, sleep, does):
        super().__init__(name, eat, sleep)
        self.does = does

    def print_rabbit_does(self):
        print(f"I am {self.does}.")


class Lion(Animal):
    def __init__(self, name, eat, sleep, does):
        super().__init__(name, eat, sleep)
        self.does = does

    def print_lion_does(self):
        print(f"I am {self.does}.")


class Cow(Animal):
    def __init__(self, name, eat, sleep, does):
        super().__init__(name, eat, sleep)
        self.does = does

    def print_cow_does(self):
        print(f"I give {self.does}.")


axel = Dog('Axel', 'meat', 'night', 'friend')
tom = Cat('Tom', 'milk', 'time', 'lazy')
bunny = Rabbit('Bunny', 'carrot', 'night', 'afraid')
simba = Lion('Simba', 'meat', 'night', 'king')
molly = Cow('Molly', 'grass', 'night', 'milk')

axel.print_animal_info()
axel.print_dog_does()
print(issubclass(Dog, Animal))

tom.print_animal_info()
tom.print_cat_does()
print(issubclass(Cat, Animal))

bunny.print_animal_info()
bunny.print_rabbit_does()
print(issubclass(Rabbit, Animal))

simba.print_animal_info()
simba.print_lion_does()
print(issubclass(Lion, Animal))

molly.print_animal_info()
molly.print_cow_does()
print(issubclass(Cow, Animal))

"""1.a. Create a new class Human and use multiple inheritance to create Centaur class, 
create an instance of Centaur class and call the common method of these classes and unique."""


class Human:
    def __init__(self, name, eat, sleep, study, work):
        self.name = name
        self.eat = eat
        self.sleep = sleep
        self.study = study
        self.work = work

    def print_human_info(self):
        print(f"My name is {self.name}. I like to eat {self.eat}. I sleep all the {self.sleep}.")

    def print_human_life(self):
        print(f"I study at {self.study}. I work in the {self.work}.")


class Centaur(Animal, Human):
    def __init__(self, name, eat, sleep, study, work, home):
        Animal.__init__(self, name, eat, sleep)
        Human.__init__(self, name, eat, sleep, study, work)
        self.home = home

    def print_centaur_home(self):
        print(f"My  home is {self.home}.")


terry = Centaur('Terry', 'meat', 'night', 'university', 'wood', 'cave')
terry.print_animal_info()
terry.print_human_life()
terry.print_centaur_home()
