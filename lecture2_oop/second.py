"""2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
a."""


class Person:
    def __init__(self):
        left_arm = Arm('Left arm')
        right_arm = Arm('Right arm')
        self.arms = [left_arm.structure, right_arm.structure]


class Arm:
    def __init__(self, structure):
        self.structure = structure


person = Person()
print(person.arms)

"""b."""


class CellPhone:
    def __init__(self, screens):
        self.screens = screens


class Screen:
    def __init__(self, menu):
        self.menu = menu


screen_1 = Screen('main screen')
screen_2 = Screen('settings screen')
screen_3 = Screen('contacts screen')
screens = [screen_1.menu, screen_2.menu, screen_3.menu]

cellphone = CellPhone(screens)
print(cellphone.screens)
