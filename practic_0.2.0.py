# Задача 1

print("Привет, мир!")

# Задача 2

print(input("имя пользователя"))

# Задача 3

number = int(input("Введите число:"))
if number % 2 == 0:
  print("четное")
else:
  print("нечетное")

# Задача 4

d = int(input())
sh = int(input())
s = d * sh
print(s)

# Задача 5

numbers = input("Введите числа через пробел: ").split()

numbers_count = 0
for x  in numbers:
    numbers_count += float(x)

average = numbers_count / len(numbers)

print(f"Среднее арифметическое: {average}")

# Задача 6

year = int(input())
if (year % 4 == 0 and year %100 != 0):
  print("високосный")
else: print("не високосный")

# Задача 7

result = "нет результата"
oper = input("введите операцию (+,-,*,/)")
num1 = int(input())
num2 = int(input())
if oper == "+":
  result = num1 + num2
elif oper == "-":
  result = num1 - num2
elif oper == "*":
  result = num1 * num2
elif oper == "/":
  if num2 != 0:
      result += num1/num2
  else:
    print("бб")
print(result)

# Практика 0.2.1

figure = input("Введите фигуру (пешка, ладья, слон, ферзь, конь, король): ").lower()
start_x = int(input("Введите стартовую координату X: "))
start_y = int(input("Введите стартовую координату Y: "))
end_x = int(input("Введите конечную координату X: "))
end_y = int(input("Введите конечную координату Y: "))

x_abs = abs(end_x - start_x)
y_abs = abs(end_y - start_y)

if figure == "пешка":
    if start_y == 2 and end_y == 4 and x_abs == 0:
        print("Ходит")
    elif y_abs == 1 and x_abs == 0:
        print("Ходит")
    else:
        print("Не может")

elif figure == "ладья":
    if x_abs == 0 or y_abs == 0:
        print("Ходит")
    else:
        print("Не ходит")

elif figure == "слон":
    if x_abs == y_abs:
        print("Ходит")
    else:
        print("Не ходит")

elif figure == "ферзь":
    if x_abs == y_abs or x_abs == 0 or y_abs == 0:
        print("Ходит")
    else:
        print('Не ходит')

elif figure == "конь":
    if (x_abs == 2 and y_abs == 1) or (x_abs == 1 and y_abs == 2):
        print('Ходит')
    else:
        print("Не ходит")

elif figure == "король":
    if x_abs <= 1 and y_abs <= 1:
        print("Ходит")
    else:
        print('Не ходит')

else:
    print('Нет фигуры')

# Практика 0.2.2

n = int(input("Введите число: "))
length = 1
count = 9
start = 1

while n > length * count:
    n -= length * count
    length += 1
    count *= 10
    start *= 10

number = start + (n - 1) // length
index = (n - 1) % length

result = str(number)[index]
print(f"ответ:{result}")