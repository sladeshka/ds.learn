"""
Задание 1

Напишите функцию, которая возвращает название валюты (поле ‘Name’) с максимальным значением курса с помощью сервиса www.cbr-xml-daily.ru...ly_json.js
"""

import requests


def get_max_currency():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()

    max_value = 0
    max_name = ""

    for currency in data['Valute'].values():
        if currency['Value'] > max_value:
            max_value = currency['Value']
            max_name = currency['Name']

    return max_name


print(get_max_currency())

"""
Задание 2

Добавьте в класс Rate параметр diff (со значениями True или False), который в случае значения True в методах курсов валют (eur, usd итд) будет возвращать не курс валюты, а изменение по сравнению в прошлым значением. Считайте, self.diff будет принимать значение True только при возврате значения курса. При отображении всей информации о валюте он не используется.
"""
class Rate:
    def __init__(self, format='value', diff=False):
        self.format = format
        self.diff = diff

    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]
            elif self.format == 'value':
                current_value = response[currency]['Value']
                previous_value = response[currency]['Previous']
                if self.diff:
                    return current_value - previous_value
                else:
                    return current_value

        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def AZN(self):
        """Возвращает курс азербайджанского маната на сегодня в формате self.format"""
        return self.make_format('AZN')

"""
Задание 3

Напишите класс Designer, который учитывает количество международных премий. Подсказки в коде занятия (“Ноутбук к лекциям «Понятие класса» + презентация”, zip-файл “Используемый ноутбук к лекциям «Понятие класса»).

Комментарий по классу Designer такой:

Напишите класс Designer, который учитывает количество международных премий для дизайнеров (из презентации: “Повышение на 1 грейд за каждые 7 баллов. Получение международной премии – это +2 балла”). Считайте, что при выходе на работу сотрудник уже имеет две премии и их количество не меняется со стажем (конечно если хотите это можно вручную менять).

Класс Designer пишется по аналогии с классом Developer из материалов занятия.
"""
class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority

        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)

    def check_if_it_is_time_for_upgrade(self):
        pass


class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1

        if self.seniority % 5 == 0:
            self.grade_up()

        return self.publish_grade()


class Designer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
        self.awards = 2

    def check_if_it_is_time_for_upgrade(self):
        points = self.awards * 2
        new_grade = 1 + (points // 7)

        while self.grade < new_grade:
            self.grade_up()

        return self.publish_grade()