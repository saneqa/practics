# Задача 1

def create_pet():
    name = input("Укажите имя для питомца: ")
    ty = input("Укажите тип питомца: ")
    age = input("Укажите тип возраст питомца: ")


    return {
        "name": name,
        "type": ty,
        "age": int(age),
        "hunger": 50,
        "happiness": 50,
        "energy": 50,
    }


def feed(pet):
    pet["hunger"] = min(100, pet["hunger"] + 20)


def play(pet):
    pet["happiness"] = min(100, pet["happiness"] + 20)
    pet["energy"] = max(0, pet["energy"] - 10)


def sleep(pet):
    pet["energy"] = min(100, pet["energy"] + 30)


def show_status(pet):
    return f"{pet['name']}: Голод: {pet['hunger']}, Счастье: {pet['happiness']}, Энергия: {pet['energy']}"


def menu():
    pet = create_pet()
    while True:
        print("\n1. Покормить питомца\n2. Поигарть с питомцем\n3. Уложить спать\n4. Статистика")
        choice = input("Выбери вариант: ")
        if choice == '1':
            feed(pet)
        elif choice == '2':
            play(pet)
        elif choice == '3':
            sleep(pet)
        elif choice == '4':
            print(show_status(pet))


menu()

# Задача 2

import random

from pyautogui import drag

def create_knight():
    return {
        "name": input("Укажите имя война: "),
        "armor": input("Укажите название брони: "),
        "weapon": input("Укажите название оружия: "),
        "damage": (5, 15),
        "health": 100
    }


def create_dragon():
    return {
        "name": random.choice(['Фаэргар', 'Люмистрелл', 'Шадрогар', 'Аэрталон', 'Кристаликс']),
        "damage": (10, 20),
        "health": 150
    }


def attack(attac, defend):
    dmg = random.randint(attac["damage"][0], attac['damage'][1])
    defend["health"] = max(0, defend["health"] - dmg)

    return dmg


def battle(knight, dragon):
    print(f'Бой между войном {knight['name']} и драконом {dragon['name']}')

    print(f"\n{knight['name']} \nЗдоровье: {knight['health']}")
    print(f"Оружие: {knight['weapon']}\nБроня: {knight['armor']}\nУрон; {knight['damage']}")

    print(f"\n{dragon['name']} \nЗдоровье: {dragon['health']}")
    print(f"Урон: {dragon['damage']}\n")

    while knight['health'] > 0 and dragon["health"] > 0:
        input('Нажмите для атаки!!!\n')

        dmg_dragon = attack(knight, dragon)
        print(f'{knight['name']} нанес {dragon['name']} {dmg_dragon} урона')

        if dragon['health'] <= 0:
            print(f'{knight['name']} победил {dragon['name']}!!!')
            break

        dmg_knight = attack(knight, dragon)
        print(f'{dragon['name']} нанес {knight['name']} {dmg_knight} урона')

        if knight['health'] <= 0:
            print(f'{dragon['name']} победил {knight['name']}!!!')
            break

    print(f"\n{knight['name']} Здоровье: {knight['health']}, {dragon['name']} Здоровье: {dragon['health']}")


def main():
    knight = create_knight()
    dragon = create_dragon()
    battle(knight, dragon)


main()