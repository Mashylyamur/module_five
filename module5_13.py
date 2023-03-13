class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def hit(self, health):
        self.health -= 20

w1 = Warrior('Warrior_one', 100)
w2 = Warrior('Warrior_two', 100)
while True:
    x = input('Введите 1, если бьет первый воин, 2 - если второй: ')
    if w1.health > 1 and w2.health > 1:
        if x == str(1):
            w2.hit(w1)
            print('Аттаковал: ', w1.name)
            print('Здоровье ', w2.name, ':', w2.health)
        elif x == str(2):
            w1.hit(w2)
            print('Аттаковал: ', w2.name)
            print('Здоровье ', w1.name, ':', w1.health)
    elif w1.health <= 0:
        print('Game over')
        print('Выиграл: ', w2.name)
        break
    elif w2.health <= 0:
        print('Game over')
        print('Выиграл: ', w1.name)
        break


