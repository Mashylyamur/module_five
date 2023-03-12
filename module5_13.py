class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def hit(self, name):
        self.health -= 20
        print('attack: ', name)
    def win(self):
        if self.health == 0:
            print('Game over')

w1 = Warrior('Warrior_one', 100)
w2 = Warrior('Warrior_two', 100)
for i in range(100):
    w1.hit(w2)
    w2.hit(w1)
    print(w1.health, w2.health)
    print(w1.name, w2.name)