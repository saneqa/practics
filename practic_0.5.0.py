# Задача 1

people = {"Alice": 25, "Bob": 30, "Charlie": 35}
name = input("Введите имя: ")
print(name, people[name])

# Задача 2

input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def count(numbers):
    ct = 0
    for number in numbers:
        if number % 2 == 0 and number > 0:
            ct += number
    return ct
print(count(input_numbers))

# Задача 3

fruits_and_flowers = {
    "apple": "green",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "violet"
}

print('Yellow fruits:')

for fruits in fruits_and_flowers:
    if fruits_and_flowers[fruits] == "yellow":
        print(fruits)

# Задача 4

x = {"a": 1, "b": 2, "c": 3}

def swap(nnn):
    result = {}

    for key in nnn:
        result.update({nnn[key]: key})

    return result

print(swap(x))

# Задача 5

data = ['apple', 'banana', 'orange', 'apple', 'apple', 'banana', 'a', 'a', 'a', 'a']

def counting(nnn):
    result = {}

    for d in nnn:
        if d not in result.keys():
            result.update({d: 1})

        else:
            result.update({d: result[d] + 1})

    return result

# Задача 6

people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}


def age_older_30(data):
    print('\nЛюди старше 30: ')
    for name in data:
        if data[name]["age"] > 30:
            print(name)

age_older_30(people_info)


def people_in_city(data):
    result = {}
    for name in data:
        town = data[name]["city"]
        if town not in result:
            result.update({town: 1})
        else:
            result.update({town: result[town] + 1})

    print('\n\nГорода и их население: ')
    for x in result:
        print(x, result[x])

people_in_city(people_info)


def profession_count(data):
    result = {}
    for name in data:
        profession = data[name]["occupation"]
        if profession not in result:
            result.update({profession: 1})
        else:
            result.update({profession: result[profession] + 1})
    print('\n\nПровессии и их количество людей: ')
    for x in result:
        print(x, result[x])
profession_count(people_info)

# Задача 7

import random

item_course = {
    "Программирование": {},
    "История России": {},
    "Математика": {},
    "Физика": {},
    "Английский язык": {},
    "Гандбол": {},
    "Основы российской государственности": {},
    "Основы проектной деятельности": {}
}

unique_id = 0


def _generate_random_feedback():
    global unique_id, item_course

    s = list(item_course.keys())
    comments = ["тест1", "тест2", "тест3", "тест4", "тест5"]

    z = random.choice(s)

    score = random.randint(1, 5)
    comment = random.choice(comments)

    item_course[z].update({unique_id: {"score": score, "comment": comment}})
    unique_id += 1


for _ in range(20):
    _generate_random_feedback()

def add_new_feedback(title, score, comment):
    global unique_id, item_course

    try:

        item_course[title].update({unique_id: {"score": score, "comment": comment}})
        unique_id += 1
        return True

    except Exception as e:
        return False


def deleted_feedback(ids, title):
    global unique_id, item_course

    try:
        item_course[title].pop(ids)
        return True

    except Exception as e:
        return False


def get_all_feedback(title):
    if len(item_course[title].keys()) > 0:
        result = []
        for x in item_course[title]:
            result.append([item_course[title][x]["score"], item_course[title][x]['comment']])

        return result
    return 0


def get_average_score(title):

    if len(item_course[title].keys()) > 0:

        count = 0
        score = 0

        for x in item_course[title]:
            score += item_course[title][x]['score']
            count += 1

        return score // count

    return 0


def check_on_number(n):
    try:
        n = int(n)
        return n
    except:
        return False


def main():
    while True:
        print('\n\n\nОтзывы о предметах')
        n = input('\n1.Добавить отзыв\n2.Просмотр отзывов\n3.Удалить отзыв\n4.Средний бал предмета\n\nУкажите вариант: ')

        n = check_on_number(n)
        if n is False:
            print('\n\n\nУкажите цифру!')
            continue

        if n == 1:
            i = 1
            s = list(item_course.keys())
            print('\n\nДоступные предметы на выбор: \n')
            for x in s:
                print(f'{i}. {x}')
                i += 1
            x = input('\nВыберите один из подходящих вариантов: ')

            x = check_on_number(x)
            if x is False:
                print('\n\n\nУкажите цифру!')
                continue

            if x > len(s):
                print('\n\n\nЭтого варианта нет в списке!')
                continue

            item = s[x - 1]

            print(f'\n\n\nВыбран предмет: {item}')
            c = input('Укажите оценку (1-5): ')

            c = check_on_number(c)
            if c is False:
                print('\n\n\nУкажите цифру!')
                continue

            if 1 <= c <= 5:
                text = input('\n\n\nОтлично, теперь введите комментарий: ')

                if add_new_feedback(item, c, text):
                    print('\n\n\nОтзыв оставлен!')
                else:
                    print('\n\n\nПроизошла ошибка, проверьте, правильно ли Вы указываете данные!!!')

            else:
                print('\n\n\nНеверная оценка!')
                continue

        elif n == 2:
            i = 1
            s = list(item_course.keys())
            print('\n\nДоступные предметы на выбор: \n')
            for x in s:
                print(f'{i}. {x}')
                i += 1
            x = input('\nВыберите один из подходящих вариантов: ')

            x = check_on_number(x)
            if x is False:
                print('\n\n\nУкажите цифру!')
                continue

            if x > len(s):
                print('\n\n\nЭтого варианта нет в списке!')
                continue

            item = s[x - 1]
            info = get_all_feedback(item)
            if info != 0:
                for score, text in info:
                    print(f'\nОценка: {score}\nКомментарий: {text}')
            else:
                print('\n\n\nОтзывы отсутствуют!')

        elif n == 3:
            i = 1
            s = list(item_course.keys())
            print('\n\nДоступные предметы на выбор: \n')
            for x in s:
                print(f'{i}. {x}')
                i += 1
            x = input('\nВыберите один из подходящих вариантов: ')

            x = check_on_number(x)
            if x is False:
                print('\n\n\nУкажите цифру!')
                continue

            if x > len(s):
                print('\n\n\nЭтого варианта нет в списке!')
                continue

            item = s[x - 1]

            s = list(item_course[item].keys())
            i = 1

            print('\n\n\nДоступные отзывы для удаления: ')
            for x in s:
                print(f'{i}. Оценка: {item_course[item][x]["score"]}\n\tКомментарий: {item_course[item][x]["comment"]}')
                i += 1


            x = input('\nВыберите один из отзывов: ')
            x = check_on_number(x)

            if x is False:
                print('\n\n\nУкажите цифру!')
                continue

            if x > len(s):
                print('\n\n\nЭтого варианта нет в списке!')
                continue

            deleted_feedback(s[x - 1], item)

        elif n == 4:
            i = 1
            s = list(item_course.keys())
            print('\n\nДоступные предметы на выбор: \n')
            for x in s:
                print(f'{i}. {x}')
                i += 1
            x = input('\nВыберите один из подходящих вариантов: ')

            x = check_on_number(x)
            if x is False:
                print('\n\n\nУкажите цифру!')
                continue

            if x > len(s):
                print('\n\n\nЭтого варианта нет в списке!')
                continue

            item = s[x - 1]

            x = get_average_score(item)
            if x != 0:
                print(f'\n\n\nСредний балл предмета: {x}')
            else:
                print('\n\n\nОтзывы на предмет отсутсвуют!')


main()
