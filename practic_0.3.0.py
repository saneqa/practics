# Задача 1

numbers = input("напишите числа через пробел: ").split(" ")

num_sum = 0
num_ave = 0
num_max = 0
num_len = 0


for x in numbers:
    num_sum += int(x)

for x in numbers:
    num_len += 1
num_ave = (num_sum/num_len)

for x in numbers:
    if int(x) > num_max:
        num_max = int(x)

print("сумма: ", num_sum)
print("ср.знач: ", num_ave)
print("макс: ", num_max)

# Задача 2

fruits = input("напишите слова через пробел: ").split(" ")
result = []
for x in range(len(fruits) -1, -1, -1):
    result.append(fruits[x])
print(result)

# Задача 3

from random import choice

all_key = {
    "order": ["дела"],
    "audio": ["музыку"],
    "films": ["фильм"],
    "serials": ["сериал"],
    "calculator": ["посчитай"]
}

data = {
    "audio": ["Метан - Нет страха", "МАША УЛЬТРАФОНК", "Кишлак - 15 препаратов", "Метан - города", "f0lk - What is love"],
    "films": ['Волка с уолл-стрит', '1+1', 'Зеленая книга', 'гарри потер'],
    "serials": ['Мистер робот', 'и снова здравствуите', "фарма", "мир дружба жвачка"]
}

answer = {
    "audio": ["Конечно, вот отличный трек: ", "Постоянно слушаю: ", "Есть у меня на примете один: ", "Да, вот: ", "Я думаю вам понравится этот: "],
    "films": ["Видел недавно интересный фильм: ", "Один из моих любимых: ", "Многие рекомендуют этот: ", "По рейтингу один из первых: "],
    "serials": ["Каждый мой вечер насыщен этим потресающим сериалом: ", "Пересматривал много раз: ", "Мне советовал друг друга друга именно его: "],
    "order": ["Вот ваш список дел: "]
}

order_list = []

while True:
    words = input("")

    main_key = None
    word_command = None

    commands = words.replace(",", "").replace("!", "") \
        .replace("?", "").replace(".", "").split(" ")

    for x in commands:
        word_command = x.lower()

        for key in all_key:
            for value in all_key[key]:
                if value == word_command:
                    main_key = key

    if main_key is None:
        print("Неверное значение, повторите попытку")

    elif main_key == "audio":
        print(choice(answer["audio"]), (choice(data["audio"])))

    elif main_key == "films":
        print(choice(answer["films"]), (choice(data["films"])))

    elif main_key == "serials":
        print(choice(answer["serials"]), (choice(data["serials"])))

    elif main_key == "order":
        text = None

        if len(order_list) > 0:
            print(choice(answer["order"]))

            i = 1
            for x in order_list:
                print(f'{i}. {x}')
                i += 1

            text = "Хотите добавить или удалить задачи? Да/Нет: "

        else:
            print("У вас нет дел")
            text = "Хотите добавить новые задачи? Да/Нет: "

        d = input(text)

        if d.lower() == "да":
            c = input("Добавить или удалить? ")
            if c.lower() == "добавить":
                v = input("Хорошо, напишите задачу которую хотите добавить: ")

                if len(v) > 1:
                    print("Новая задача успешно добавлена!")
                    order_list.append(v)
                else:
                    print("Указано неккоректно, повторите запрос")

            elif c.lower() == "удалить":
                v = input("Выберите номер задачи, которую желаете удалить: ")

                if v.isdigit():
                    try:
                        _ = order_list.pop(int(v) - 1)
                        print("Задача успешно удалена!")

                    except IndexError:
                        print("Задачи под таким номером не найдено")
                else:
                    print("Номер указан неккоректно, повторите запрос")
        else:
            print("Возвращаю в главное меню.")


    elif main_key == "calculator":
        print("Укажите выражение которое хотите выполнить\nФункции которые я поддерживаю +, -, *, / \
        \nКаждый элемент нужно написать через пробел\nА так-же подсчет идет по очереди")
        d = input("")

        # d =  5 + 5 + 5

        b = d.split(" ")
        num = [] # 5 5 5
        operations = [] # +  +
        for z in b:
            if z.isdigit():
                num.append(int(z))
            else:
                operations.append(z)

        # 5 + 5 + 5
        express = 0
        i = 0

        for x in num:
            if i == 0:
                express = x
                i += 1
                continue

            if operations[i - 1] == "+":
                express = express + num[i]

            elif operations[i - 1] == "-":
                express = express - num[i]

            elif operations[i - 1] == "*":
                express = float(express * num[i])

            elif operations[i - 1] == "/":
                express = float(express / num[i])

            i += 1
        print("Вот значение вашего выражение:", express)

    else:
        print("неверная операция")

# Задача 4

from random import choice

score = [0, 0]

while score[0] != 3 and score[1] != 3:
    word = input("Выберите камень/ножницы/бумага: ")
    word1 = choice(["камень", "ножницы", "бумага"])

    print("Игрок: ", word)
    print("Компьютер: ", word1)

    if word == word1:
        pass

    elif word == "камень" and word1 == "ножницы":
        score[0] += 1

    elif word == "ножницы" and word1 == "бумага":
        score[0] += 1

    elif word == "бумага" and word1 == "камень":
        score[0] += 1

    else:
        score[1] += 1

    print(score[0], ":", score[1])

if score[0] == 3:
    print("По результатам победил пользователь")
else:
    print("Победил компьютер")

# Задача 5

from random import choice
import os

words = ['очки', 'арбуз', 'завод', 'квадрат', 'азбука']

secret_word = choice(words)
secret_list = []

for x in range(len(secret_word)):
    secret_list.append("*")

score = 0
wrong = 0

human = [
    """
     ------
     |    |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ----------
    """,
    r"""
     ------
     |    |
     |    O
     |   /|\
     |
     |
    ----------
    """,
    r"""
     ------
     |    |
     |    O
     |   /|\
     |   /
     |
    ----------
    """,
    r"""
     ------
     |    |
     |    O
     |   /|\
     |   / \
     |
    ----------
    """
]


while wrong <= 6:
    os.system("cls")
    word = ""

    for x in secret_list:
        word += x

    print(human[wrong])
    print("Кол-во очков:", score)
    print("Кол-во ошиибок:", wrong)
    print("")

    if "*" in secret_list:

        if wrong >= 6:
            print("Вы проиграли")
            break

        print("Загаданное слово: ", word)

        character = input("Введите букву или слово: ").strip()

        if len(character) > 1:
            if character == secret_word:
                print("")
                print("Вы победили!!!")
                print("")
                score += len(secret_word)
                i = 0

                for x in secret_word:
                    secret_list[i] = x
                    i += 1
            else:
                print("Неверное слово")
                wrong += 1
        else:
            if character in secret_word:
                i = 0
                for x in secret_word:
                    if x == character:
                        secret_list[i] = character
                    i += 1

                if "*" not in secret_list:
                    print("")
                    print("Вы победили!!!")
                    score += len(secret_word)

            else:
                wrong += 1
                print("Неверная буква")

    else:

        asc = input("Хотите продолжить?")
        if asc.lower() == "да":
            secret_word = choice(words)
            secret_list = []
            wrong = 0

            for x in range(len(secret_word)):
                secret_list.append("*")

        else:
            print("Всего хорошего!")
            break