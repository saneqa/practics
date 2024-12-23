# Задача 1

wish_list = input().split(' ')

no_duplicates = []
for x in wish_list:
    if x not in no_duplicates:
        no_duplicates.append(x)


s = ''
for x in no_duplicates:
    s += f'{x} '

print(s)

# Задача 2

def find_simple_numbers(a, b):
    wish_list = []
    a = int(a)
    b = int(b)
    for x in range(a, b + 1):
        ct = 0

        for y in range(1, (x // 2 + 1)):
            if x % y == 0:
                ct += 1

        if ct == 1:
            wish_list.append(x)

    return wish_list


x, c = input().split(', ')

print(', '.join(str(x) for x in find_simple_numbers(x, c)))

# Задача 3

keys = ['a', 'b', 'c', 'e' ]
values = [1, 2, 3, 4]


def union_list(k, v):
    result = {}
    i = 0
    for x in k:
        result.update({x: v[i]})
        i += 1

    return result


print(union_list(keys, values))

# Задача 4

numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = {"mean": 0.0, "median": 0, "mode": 0, "sum": 0}


def get_sum(num_list):
    s = 0
    for x in num_list:
        s += x

    result.update({"sum": s})


def get_avg(num_list):
    ct = 0
    for _ in num_list:
        ct += 1

    mean = result["sum"] / ct
    result.update({"mean": mean})


def get_median(num_list):
    ct = 0
    for _ in num_list:
        ct += 1

    medi = num_list[ct // 2]
    result.update({"median": medi})


def get_mode(num_list):
    c = {}

    for x in num_list:
        if x not in c.keys():
            c.update({x: 1})
        else:
            c.update({x: c[x] + 1})

    m = 0
    ms = 0

    for x in c.keys():
        if c[x] > ms:
            m = x
            ms = c[x]

    result.update({"mode": m})


get_sum(numbers)
get_avg(numbers)
get_median(numbers)
get_mode(numbers)

print(result)

# Задача 5

text = 'Страдание и боль всегда обязательны для широкого сознания и глубокого сердца.'.strip(".").split(" ")

mw = 0
mn = 0
ml = 0

c = 1
for x in text:
    i = 0

    for y in x:
        i += 1

    if i > ml:
        ml = i
        mw = x
        mn = c

    c += 1

print(f"Самое длинное слово с номером {mn}: {mw}")

# Задача 6

students = {}


def add_student_info(name, scores):
    if name not in students:
        students[name] = scores
    else:
        students[name].extend(scores)


def avg_students(name):
    if name in students:
        if students[name]:
            result = sum(students[name]) / len(students[name])
            return result

    return 0


def all_avg_students():
    result = []

    for name in students:
        result.append([name, avg_students(name)])

    return result


def get_student_info(name):
    if name in students:
        data = avg_students(name)
        return name, students[name], data

    return 0


add_student_info('Alex', [5, 3, 5, 5, 5])
add_student_info('Dima', [2, 5, 4, 3, 5])
add_student_info('Nikita', [4, 1, 4, 2, 4])

print('Информация о студенте Alex')
x = get_student_info('Alex')
print(f'Имя: {x[0]}\nОценки: {x[1]}\nСр.балл: {x[2]}\n')

print('Информация о среднем бале студентов')
x = all_avg_students()
for z in x:
    print(f'{z[0]}\nСр.балл: {z[1]}\n')

print('Средний бал студента Dima')
print(avg_students('Dima'))

# Задача 7

import random

questions = [
    {'quest': 'Столица Канады', 'answer': 'оттава', 'point': 6},
    {'quest': 'Сколько законов Ньютона существует? (Ответ записать цифрой)', 'answer': '3', 'point': 2},
    {'quest': 'Как называется самая глубокая точка мирового океана?', 'answer': 'марианская впадина', 'point': 5},
    {'quest': 'Земля вращается вокруг своей оси один раз в _ часов. (Ответ записать цифрой)', 'answer': '24',
     'point': 4},
    {'quest': 'Из какой страны Архимед?', 'answer': 'греция', 'point': 6},
    {'quest': 'Пустыня в Африке?', 'answer': 'сахара', 'point': 3},
    {'quest': 'Доска для арифметических вычислений в Древней Греции', 'answer': 'абак', 'point': 10},
    {'quest': 'Бывает сливочное, бывает оливковое', 'answer': 'масло', 'point': 1},
    {'quest': 'Что идет, не двигаясь с места?', 'answer': 'время', 'point': 4},
    {'quest': 'Ансамбль из 4 исполнителей', 'answer': 'квартет', 'point': 7},
    {'quest': 'Что означает ДНК?', 'answer': 'дезоксирибонуклеиновая кислота', 'point': 9},
    {'quest': 'В греческой мифологии: герой, совершивший 12 подвигов', 'answer': 'геракл', 'point': 8},
]


def add_new_quest(quest, answer, point):
    questions.append({"quest": quest, "answer": answer, 'point': point})


def shuffle_question():
    random.shuffle(questions)


def start_game():
    print('\n\nНачало викторины!\n')
    shuffle_question()
    points = 0

    for quest in questions:
        print('Вопрос: ', quest['quest'])
        ans = input('Ваш ответ: ')

        if ans.lower() == quest['answer'].lower():
            print('Ответ верный!\n')
            points += quest['point']

        else:
            print(f'К сожалению, ответ не правильный! Правильный ответ: {quest["answer"]}\n')

    return points


def main():
    print('\n\nВикторина\n\n1.Запустить викторину\n2.Добавить новый вопрос')
    c = input('Выберите: ')

    if c == '1':
        total = start_game()
        print(f'Вы смогли набрать: {total}')

    elif c == '2':
        q = input("Введите ваш вопрос: ")
        a = input("Введите ответ на вопрос: ")
        p = int(input("Укажите кол-во баллов этого вопроса: "))
        add_new_quest(q, a, p)
        print('Вопрос успешно добавлен!')


main()