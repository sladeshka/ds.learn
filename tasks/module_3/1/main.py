import math
"""
Задание 1

Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
Напишите код, который проверяет какая из этих строк длиннее.

Примеры работы программы:1.
"""

phrase_1 = "Насколько проще было бы писать программы, если бы не заказчики"
phrase_2 = "640Кб должно хватить для любых задач. Билл Гейтс (по легенде)"
len_phrase_1 = len(phrase_1)
len_phrase_2 = len(phrase_2)
if len_phrase_1 > len_phrase_2:
    print("Фраза 1 длиннее фразы 2")
elif len_phrase_1 < len_phrase_2:
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")

"""
Результат:
Фраза 1 длиннее фразы 2
"""

phrase_1 = "640Кб должно хватить для любых задач. Билл Гейтс (по легенде)"
phrase_2 = "Насколько проще было бы писать программы, если бы не заказчики"
len_phrase_1 = len(phrase_1)
len_phrase_2 = len(phrase_2)
if len_phrase_1 > len_phrase_2:
    print("Фраза 1 длиннее фразы 2")
elif len_phrase_1 < len_phrase_2:
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")

"""
Результат:
Фраза 2 длиннее фразы 1
"""

phrase_1 = "Насколько проще было бы писать программы, если бы не заказчики"
phrase_2 = "Насколько проще было бы писать программы, если бы не заказчики"
len_phrase_1 = len(phrase_1)
len_phrase_2 = len(phrase_2)
if len_phrase_1 > len_phrase_2:
    print("Фраза 1 длиннее фразы 2")
elif len_phrase_1 < len_phrase_2:
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")

"""
Результат:
Фразы равной длины
"""

"""
Задание 2

Дана переменная, в которой хранится число (год). Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.

Пример работы программы:
"""

year = 2020
if year % 4 != 0:
    print("Обычный год")
elif year % 100 != 0:
    print("Високосный год")
elif year % 400 == 0:
    print("Високосный год")
else:
    print("Обычный год")

"""
Результат:
Високосный год
"""

year = 2019
if year % 4 != 0:
    print("Обычный год")
elif year % 100 != 0:
    print("Високосный год")
elif year % 400 == 0:
    print("Високосный год")
else:
    print("Обычный год")

"""
Результат:
Обычный год
"""

"""
Задание 3

Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.
Пример работы программы:
Введите день:
30
Введите месяц:
Август
"""
months = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12
}
day_input = int(input("Введите день: "))
month_input = input("Введите месяц: ").lower()
month = months.get(month_input)
if (month == 1 and day_input >= 20) or (month == 2 and day_input <= 18):
    sign = 'Водолей'
elif (month == 2 and day_input >= 19) or (month == 3 and day_input <= 20):
    sign = 'Рыбы'
elif (month == 3 and day_input >= 21) or (month == 4 and day_input <= 20):
    sign = 'Овен'
elif (month == 4 and day_input >= 21) or (month == 5 and day_input <= 20):
    sign = 'Телец'
elif (month == 5 and day_input >= 21) or (month == 6 and day_input <= 21):
    sign = 'Близнецы'
elif (month == 6 and day_input >= 22) or (month == 7 and day_input <= 22):
    sign = 'Рак'
elif (month == 7 and day_input >= 23) or (month == 8 and day_input <= 22):
    sign = 'Лев'
elif (month == 8 and day_input >= 23) or (month == 9 and day_input <= 22):
    sign = 'Дева'
elif (month == 9 and day_input >= 23) or (month == 10 and day_input <= 22):
    sign = 'Весы'
elif (month == 10 and day_input >= 23) or (month == 11 and day_input <= 21):
    sign = 'Скорпион'
elif (month == 11 and day_input >= 22) or (month == 12 and day_input <= 21):
    sign = 'Стрелец'
else:
    sign = 'Козерог'
print(f"Ваш знак зодиака: {sign}")
"""
Результат:
Ваш знак зодиака: Дева
"""

"""
Введите день:
29
Введите месяц:
Октябрь
"""
day_input = int(input("Введите день: "))
month_input = input("Введите месяц: ").lower()
month = months.get(month_input)
if (month == 1 and day_input >= 20) or (month == 2 and day_input <= 18):
    sign = 'Водолей'
elif (month == 2 and day_input >= 19) or (month == 3 and day_input <= 20):
    sign = 'Рыбы'
elif (month == 3 and day_input >= 21) or (month == 4 and day_input <= 20):
    sign = 'Овен'
elif (month == 4 and day_input >= 21) or (month == 5 and day_input <= 20):
    sign = 'Телец'
elif (month == 5 and day_input >= 21) or (month == 6 and day_input <= 21):
    sign = 'Близнецы'
elif (month == 6 and day_input >= 22) or (month == 7 and day_input <= 22):
    sign = 'Рак'
elif (month == 7 and day_input >= 23) or (month == 8 and day_input <= 22):
    sign = 'Лев'
elif (month == 8 and day_input >= 23) or (month == 9 and day_input <= 22):
    sign = 'Дева'
elif (month == 9 and day_input >= 23) or (month == 10 and day_input <= 22):
    sign = 'Весы'
elif (month == 10 and day_input >= 23) or (month == 11 and day_input <= 21):
    sign = 'Скорпион'
elif (month == 11 and day_input >= 22) or (month == 12 and day_input <= 21):
    sign = 'Стрелец'
else:
    sign = 'Козерог'
print(f"Ваш знак зодиака: {sign}")
"""
Результат:
Ваш знак зодиака: Скорпион
"""

"""
Задание 4

Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):
Используйте следующие правила:
если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран “Коробка №1”;
если хотя бы одно из измерений больше 2 метров, то выводите “Упаковка для лыж”;
если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите “Коробка №2”;
во всех остальных случаях выводите “Коробка №3”.
Пример работы программы:
"""

width = 15
length = 55
height = 15
if width > 200 or length > 200 or height > 200:
    print("Упаковка для лыж")
elif width <= 15 and length <= 15 and height <= 15:
    print("Коробка №1")
elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
    print("Коробка №2")
else:
    print("Коробка №3")

"""
Результат:
Коробка №3
"""

width = 45
length = 205
height = 45
if width > 200 or length > 200 or height > 200:
    print("Упаковка для лыж")
elif width <= 15 and length <= 15 and height <= 15:
    print("Коробка №1")
elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
    print("Коробка №2")
else:
    print("Коробка №3")

"""
Результат:
Упаковка для лыж
"""

"""
Задание 5
Дана переменная, в которой хранится шестизначное число (номер проездного билета). Напишите программу, которая будет определять, является ли данный билет “счастливым”. Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.
Примеры работы программы:
"""
number = 123456
number_str = str(number)
first = number_str[:3]
last = number_str[3:]

sum_first = sum(int(digit) for digit in first)
sum_last = sum(int(digit) for digit in last)

if sum_first == sum_last:
    print("Счастливый билет!")
else:
    print("Несчастливый билет.")
"""
Результат:
Несчастливый билет
"""

number = 123321
number_str = str(number)
first = number_str[:3]
last = number_str[3:]

sum_first = sum(int(digit) for digit in first)
sum_last = sum(int(digit) for digit in last)

if sum_first == sum_last:
    print("Счастливый билет!")
else:
    print("Несчастливый билет.")
"""
Результат:
Счастливый билет
"""

"""
Задание 6

Напишите программу, которая сможет вычислять площади трех фигур (круг, треугольник и прямоугольник). Тип фигуры запрашиваем через пользовательский ввод, после чего делаем запрос характеристик фигуры:

если пользователь выбрал круг, запрашиваем его радиус,
если треугольник – длины трех его сторон;
если прямоугольник – длины двух его сторон.
Пример работы программы: 1.

Введите тип фигуры:
Круг

Введите радиус круга:
10
Результат:
Площадь круга: 314.16

Введите тип фигуры:
Треугольник

Введите длину стороны A:
2

Введите длину стороны B:
2

Введите длину стороны C:
3
Результат:
Площадь треугольника: 1.98
"""

# Функция для вычисления площади круга
def circle_area(radius):
    return round(math.pi * radius ** 2, 2)

# Функция для вычисления площади треугольника по формуле Герона
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    if s <= 0 or (s - a) <= 0 or (s - b) <= 0 or (s - c) <= 0:
        return None
    area_squared = s * (s - a) * (s - b) * (s - c)
    if area_squared > 0:
        return round(math.sqrt(area_squared), 2)
    else:
        return None

# Функция для вычисления площади прямоугольника
def rectangle_area(a, b):
    return round(a * b, 2)

# Основная программа
figure_type = input("Введите тип фигуры (Круг, Треугольник, Прямоугольник): ").lower()

if figure_type == "круг":
    radius = float(input("Введите радиус круга: "))
    area = circle_area(radius)
    print(f"Площадь круга: {area}")
elif figure_type == "треугольник":
    a = float(input("Введите длину стороны A: "))
    b = float(input("Введите длину стороны B: "))
    c = float(input("Введите длину стороны C: "))

    # Проверка возможности формирования треугольника
    if (a + b > c) and (a + c > b) and (b + c > a):
        area = triangle_area(a, b, c)
        if area is not None:
            print(f"Площадь треугольника: {area}")
        else:
            print("Ошибка вычисления площади. Проверьте корректность данных.")
    else:
        print("Нельзя образовать треугольник с такими сторонами.")
elif figure_type == "прямоугольник":
    a = float(input("Введите длину стороны A: "))
    b = float(input("Введите длину стороны B: "))
    area = rectangle_area(a, b)
    print(f"Площадь прямоугольника: {area}")
else:
    print("Неверный тип фигуры. Доступные варианты: Круг, Треугольник, Прямоугольник.")