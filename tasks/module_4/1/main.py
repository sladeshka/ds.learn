import pandas as pd

"""
Задание 1

Датасет для домашнего задания находится в материалах занятия - файлы для домашнего задания «Библиотека Pandas».

Определите, какому фильму было выставлено больше всего оценок 5.0.
"""

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
ratings_5 = ratings[ratings['rating'] == 5.0]
movie_counts = ratings_5.groupby('movieId').size()
top_movie_id = movie_counts.idxmax()
top_movie_title = movies[movies['movieId'] == top_movie_id]['title'].values[0]

print(f"Фильму '{top_movie_title}' было выставлено больше всего ({movie_counts.max()}) оценок 5.0.")

"""
Задание 2

По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 год. 

Не учитывайте в расчётах отрицательные значения quantity.
"""

power = pd.read_csv('power.csv')
baltic_countries = ['Latvia', 'Lithuania', 'Estonia']
categories = [4, 12, 21]
filtered_power = power[(power['country'].isin(baltic_countries)) &
                       (power['category'].isin(categories)) &
                       (power['year'] >= 2005) &
                       (power['year'] <= 2010) &
                       (power['quantity'] > 0)]
total_quantity = filtered_power['quantity'].sum()

print(f"Суммарное потребление стран Прибалтики категорий {categories} за период с 2005 по 2010 год: {total_quantity}")

"""
Задание 3

Выберите страницу любого сайта с табличными данными. 

Импортируйте таблицы в pandas DataFrame. 

Вы можете взять любые страницы.

Примеры страниц:

"""

tables = pd.read_html("http://www.pogodaiklimat.ru/history/26063.htm")
years_table = tables[0]
temperature_table = tables[1]
weather_over_the_years = pd.concat([years_table, temperature_table], axis=1)
print(weather_over_the_years.head())