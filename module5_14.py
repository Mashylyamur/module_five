from random import randint
class Warrior:
    def __init__(self, name, health, end, armor):
        self.name = name
        self.health = health
        self.end = end
        self.armor = armor
    def attack(self):
        self.health -= (randint(10, 30))
        self.end -= 10
    def protec_attack(self):
        self.health -= (randint(0, 20))
        self.armor -= (randint(0, 10))

w1 = Warrior('Warrior_one', 100, 100, 100)
w2 = Warrior('Warrior_two', 100, 100, 100)



