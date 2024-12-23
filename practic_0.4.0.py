# Задача 1

products = int(input("Количество товара: "))
promocode = input("Введите промокод: ")
cost = int(input("Введите стоимость единицы товара:  "))


def counting(cost, products, promocode):
    result = 0
    discont = 0

    if products > 1000 and products <= 5000:
        if promocode == "SUPERDISCOUNT":
            discont = 10
            result = products * cost * (1 - 0.1)
        else:
            result = products * cost * (1 - 0.05)
            discont = 5

    elif products > 5000:
        if promocode == "SUPERDISCOUNT":
            discont = 20
            result = products * cost * (1 - 0.2)
        else:
            result = products * cost * (1 - 0.15)
            discont = 15

    else:
        result = products * cost

    return result, discont


result, discont = counting(cost, products, promocode)
print("Ваша скидка: ", discont, "%")
print("Итоговая сумма: ", result)

# Задача 2

numbers = input("Введите числа:")


def split(text, symbol):
    result = []
    current = ""

    for x in text:
        if x == symbol:
            if current != "":
                result.append(current)
            current = ""
        else:
            current += x

    if current != "":
        result.append(current)

    return result


def filter(num):
    wishlist = []
    for y in num:
        if int(y) > 0:
            wishlist.append(y)
    return wishlist


numbers = split(numbers, " ")
x = filter(num = numbers)
result = ""
for z in x:
    result += z
    result += " "

print(result)

# Задача 3

numbers = input("Введите числа:")


def split(text, symbol):
    result = []
    current = ""

    for x in text:
        if x == symbol:
            if current != "":
                result.append(current)
            current = ""
        else:
            current += x

    if current != "":
        result.append(current)

    return result


numbers_list = split(numbers, " ")
number1 = int(numbers_list[0])
number2 = int(numbers_list[1])


def NOD():
    divider = 0
    max_number = 0

    if number1 > number2:
        max_number = number1
    else:
        max_number = number2

    for x in range(1, max_number):
        if number1 % x == 0 and number2 % x == 0:
            divider = x

    return divider

x = NOD()
print(x)

# Задача 4

def string_to_list(text: str) -> list:
    result = []

    text = text.split(" ")

    for word in text:
        if result:
            if word not in result[0]:
                i = 0
                for x in text:
                    if x == word:
                        i += 1

                result.append([word, i])

        else:
            i = 0
            for x in text:
                if x == word:
                    i += 1

            result.append([word, i])

    return result


data = string_to_list("apple banana apple")

for x in data:
    print(f'{x[0]}: {x[1]}')

# Задача 5

def detector_anagram(text1: str, text2: str):
    text1 = text1.strip().lower()
    text2 = text2.strip().lower()

    i1 = 0
    i2 = 0

    text1_char = []
    text2_char = []

    for x in text1:
        i1 += 1
        text1_char += x

    for x in text2:
        i2 += 1
        text2_char += x

    if i1 != i2:
        return False

    for x in text1_char:
        i = 0

        for z in text1_char:
            if x == z:
                i += 1

        for z in text2_char:
            if x == z:
                i += 1

        if i % 2 != 0:
            return False

    return True


word1 = "listen"
word2 = "silent"

if detector_anagram(word1, word2) is True:
    print('True')
else:
    print("False")

# Задача 6

def shifr(word: str, number: int):
    word = word.lower()
    char = "abcdefghijklmnopqrstuvwxyz"

    result = ""

    for x in word:
        if x in char:
            z = char.index(x)
            c = z + number
            c = c % 26

            result += char[c]
        else:
            result += x

    return result

def deshifr(word: str, number: int):
    word = word.lower()

    char = "abcdefghijklmnopqrstuvwxyz"

    result = ""

    for x in word:
        if x in char:
            z = char.index(x)
            c = z - number
            c = c % 26

            result += char[c]
        else:
            result += x

    return result


x = shifr('text!', 3)
print(x)
print(deshifr(x, 3))

# Задача 7

import time

bank_accounts = []

checks = []

unique_id = 0
unique_id_check = 0


def tracker(ids: int, operation: str, count: int, other: str):
    global bank_accounts, checks, unique_id_check
    for account in bank_accounts:
        if account[0] == ids:
            bank_accounts.remove(account)

            checks.append([unique_id_check, operation, count, other])
            account[2].append(unique_id_check)

            bank_accounts.append(account)

            unique_id_check += 1
            return


def create_account():
    global bank_accounts, unique_id

    bank_accounts.append([unique_id, 0, []])
    unique_id += 1

    return unique_id - 1


def give_take(ids: int, count: int, operation: str):
    global bank_accounts

    for account in bank_accounts:
        if account[0] == ids:
            if operation == 'deposit':
                bank_accounts.remove(account)
                account[1] += count
                bank_accounts.append(account)

                tracker(ids, 'пополнение', count, time.time())
                return None

            else:
                bank_accounts.remove(account)
                account[1] -= count
                bank_accounts.append(account)

                tracker(ids, 'снятие', count, time.time())

                return None


def check_current_balance(ids: int):
    for account in bank_accounts:
        if account[0] == ids:
            return account[1]


def transfer_balance(ids_from: int, ids_where: int, count: int):
    global bank_accounts
    account_from = None
    account_where = None

    for account in bank_accounts:
        if account[0] == ids_from:
            account_from = account
        if account[0] == ids_where:
            account_where = account

    bank_accounts.remove(account_from)
    bank_accounts.remove(account_where)
    account_where[1] += count
    account_from[1] -= count

    bank_accounts.append(account_from)
    bank_accounts.append(account_where)

    x = time.time()

    tracker(ids_from, 'перевод', count, x)
    tracker(ids_where, 'пополнение', count, x)


def main():
    while True:
        n = int(input('\n\n\nБанк меню\n\n1.Создать аккаунт\n2.Внести средства\n3.Снять средства\n4.Перевести\n5.Проверить баланс аккаунтаа\n6.Вывести чеки аккаунта\n\nВыберите:'))

        if n == 1:
            number_account = create_account()
            print('Вы успешно создали аккаунт. Его уникальный номер:', number_account)

        if n == 2:
            id_acc = int(input('Укажите номер аккаунта: '))
            count_acc = int(input('Укажите сумму на которую Вы хотите сделать операцию: '))

            give_take(id_acc, count_acc, "deposit")

            print('Вы успешно совершили операцию')

        if n == 3:
            id_acc = int(input('Укажите номер аккаунта: '))
            count_acc = int(input('Укажите сумму на которую Вы хотите сделать операцию: '))

            give_take(id_acc, count_acc, "withdraw")

            print('Вы успешно совершили операцию')

        if n == 4:
            id_acc = int(input('Укажите номер аккаунта с которого хотите снять средства: '))
            id2_acc = int(input('Укаажите номер аккаунта который хотите пополнить: '))

            count_acc = int(input('Укажите сумму на которую Вы хотите сделать операцию: '))

            transfer_balance(id_acc, id2_acc, count_acc)

            print('Вы успешно совершили операцию')

        if n == 5:
            id_acc = int(input('Укажите номер аккаунта у которого хотите проверить баланс: '))

            print('Баланс данного аккаунта: ', check_current_balance(id_acc))

        if n == 6:
            id_acc = int(input('Укажите аккаунт у которого хотите получить список транзакций: '))

            for account in bank_accounts:
                if account[0] == id_acc:
                    for check in checks:
                        if check[0] in account[2]:
                            print(f'ID операции: {check[0]}\nОперация: {check[1]}\nСумма: {check[2]}\nВремя операции: {check[3]}')


main()