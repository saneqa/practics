# Задача 1

class Recktangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def square(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def show(self):
        print(f"Ширина: {self.width}, Высота: {self.height}")


rect = Recktangle(10, 50)
rect.show()
print(f"Площадь: {rect.square()}")
print(f"Периметр: {rect.perimeter()}")

# Задача 2

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0


    def deposit(self, amount):
        self.balance += amount
        print(f"Депозит {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято {amount}")
        else:
            print("Недостаточно средств!")

    def get_balance(self):
        return self.balance


account = BankAccount("Ден")

print(f"Владелец: {account.account_holder}")
print(f"Стартовый баланс: {account.get_balance()}")

account.deposit(100)
account.withdraw(30)
account.withdraw(100)

print(f"Текущий баланс: {account.get_balance()}")

# Задача 3

import random


class Knight:
    def __init__(self):
        self.name = input("Укажите имя война: ")
        self.armor = input("Укажите название брони: ")
        self.weapon = input("Укажите название оружия: ")
        self.damage = (5, 15)
        self.health = 100




class Dragon:
    def __init__(self):
        self.name = random.choice(['Фаэргар', 'Люмистрелл', 'Шадрогар', 'Аэрталон', 'Кристаликс'])
        self.damage = (10, 20)
        self.health = 150




class Battle:
    def __init__(self, knight, dragon):
        self.knight = knight
        self.dragon = dragon


    def attack(self, attac, defend):
        dmg = random.randint(attac.damage[0], attac.damage[1])
        defend.health = max(0, defend.health - dmg)
        return dmg

    def start(self):
        print(f'Бой между войном {self.knight.name} и драконом {self.dragon.name}')

        print(f"\n{self.knight.name} \nЗдоровье: {self.knight.health}")
        print(f"Оружие: {self.knight.weapon}\nБроня: {self.knight.armor}\nУрон: {self.knight.damage}")

        print(f"\n{self.dragon.name} \nЗдоровье: {self.dragon.health}")
        print(f"Урон: {self.dragon.damage}\n")

        while self.knight.health > 0 and self.dragon.health > 0:
            input('Нажмите для атаки!!!\n')

            dmg_dragon = self.attack(self.knight, self.dragon)
            print(f'{self.knight.name} нанес {self.dragon.name} {dmg_dragon} урона')

            if self.dragon.health <= 0:
                print(f'{self.knight.name} победил {self.dragon.name}!!!')
                break

            dmg_knight = self.attack(self.dragon, self.knight)
            print(f'{self.dragon.name} нанес {self.knight.name} {dmg_knight} урона')

            if self.knight.health <= 0:
                print(f'{self.dragon.name} победил {self.knight.name}!!!')
                break

        print(f"\n{self.knight.name} Здоровье: {self.knight.health}, {self.dragon.name} Здоровье: {self.dragon.health}")




def main():
    knight = Knight()
    dragon = Dragon()
    battle = Battle(knight, dragon)
    battle.start()


main()