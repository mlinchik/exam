import random

class Person:
    name = ''
    hp = 0
    mood = 0
    money = 0

    def __init__(self, name='', hp=0, mood=0, money=0):
        self.name = name
        self.hp = hp
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Здоровье: {self.hp}\n' \
               f'Настроение: {self.mood}\n' \
               f'Капитал: {self.money}\n'

    def change_state(self):
        self.money += 40
        self.mood -= 20
        self.hp -= 30
        self.money += random.randint(-90, 100)
        self.mood += random.randint(-60, 100)
        self.hp += random.randint(-70, 100)

    def go_to_park(self):
        self.mood += 20

    def go_to_work(self):
        self.money += 50

    def go_to_hospital(self):
        self.hp += 30
