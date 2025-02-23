"""
Задание 1

Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:

The Moscow Times — Wednesday, October 2, 2002
The Guardian — Friday, 11.10.13
Daily News — Thursday, 18 August 1977
"""
from datetime import datetime, timedelta

print(datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y'))
print(datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y'))
print(datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y'))

"""
Задание 2

Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:

stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]

Напишите функцию, которая проверяет эти даты на корректность. То есть для каждой даты возвращает True — дата корректна или False — некорректная.
"""

stream = ['2018-04-02', '2018-02-29', '2018-19-02']
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


for date in stream:
    print(f"{date}: {is_valid_date(date)}")
"""
Задание 3

Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. Даты должны вводиться в формате YYYY-MM-DD. В случае неверного формата или при start_date > end_date должен возвращаться пустой список.
"""
def date_range(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        return []

    if start > end:
        return []

    dates = []
    current = start
    while current <= end:
        dates.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)
    return dates

print(date_range('2025-02-01', '2025-02-23'))
print(date_range('2025-02-41', '2025-02-23'))


"""
Условие задачи

Напишите функцию, которая будет возвращать акроним по переданной в неё строке со словами.

Примеры работы программы:
some_words = 'Информационные технологии’
Результат: ИТ

some_words = 'Near Field Communication’
Результат: NFC

Впишите своё решение вместо «…».

Важно: не удаляйте код ниже, а дополните его. Функция необходима для проверки вашего решения. Функция принимает и возвращает строку.
"""

import re

def acronym(some_words):
   return ''.join(some_words[0].upper() if some_words else '' for some_words in some_words.split())

print(acronym('Информационные технологии'))
print(acronym('Near Field Communication'))