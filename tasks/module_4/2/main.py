import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

"""
Задание 1

Напишите функцию, которая классифицирует фильмы из материалов занятия по правилам:

* оценка 2 и ниже — низкий рейтинг;

* оценка 4 и ниже — средний рейтинг;

* оценка 4.5 и 5 — высокий рейтинг.

Результат классификации запишите в столбец class.
"""

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
avg_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
def classify_rating(rating):
    if rating <= 2:
        return 'низкий рейтинг'
    elif rating <= 4:
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'
avg_ratings['class'] = avg_ratings['rating'].apply(classify_rating)
movies_with_class = pd.merge(movies, avg_ratings[['movieId', 'class']], on='movieId')
print(movies_with_class[['title', 'class']].head())

"""
Задание 2

Используйте файл keywords.csv.

Нужно написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определённому региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется название этого региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.

Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:

geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

Результат классификации запишите в отдельный столбец region.
"""

keywords = pd.read_csv('keywords.csv')
geo_data = {
    'Центр': ['москва', 'тула', 'ярославль'],
    'Северо-Запад': ['петербург', 'псков', 'мурманск'],
    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}
def classify_region(keyword):
    keyword_lower = keyword.lower()
    for region, cities in geo_data.items():
        if any(city in keyword_lower for city in cities):
            return region
    return 'undefined'

keywords['region'] = keywords['keyword'].apply(classify_region)
print(keywords.head())
keywords_with_region = keywords[keywords['region'] != 'undefined']
print(keywords_with_region.head())

"""
Задание 3 (бонусное)

Есть мнение, что раньше снимали настоящее кино, не то что сейчас. Ваша задача — проверить это утверждение, используя файлы с рейтингами фильмов из прошлого домашнего занятия: файл movies.csv и ratings.csv из базы. Нужно проверить, верно ли, что с ростом года выпуска фильма его средний рейтинг становится ниже.

Вы не будете затрагивать субьективные факторы выставления этих рейтингов, а пройдётесь по алгоритму:

1. В переменную years запишите список из всех годов с 1950 по 2010 года.

2. Напишите функцию production_year, которая каждой строке из названия фильма выставляет год выпуска. Не все названия фильмов содержат год выпуска в одинаковом формате, поэтому используйте алгоритм:

* для каждой строки пройдите по всем годам списка years;
* если номер года присутствует в названии фильма, то функция возвращает этот год, как год выпуска;
* если ни один из номеров года списка years не встретился в названии фильма, то возвращается 1900 год.

3. Запишите год выпуска фильма по алгоритму пункта 2 в новый столбец ‘year’.

4. Посчитайте средний рейтинг всех фильмов для каждого значения столбца ‘year’ и отсортируйте результат по убыванию рейтинга.
"""

def production_year(title):
    years = list(range(1950, 2011))
    for year in years:
        if f'({year})' in title or f' {year} ' in title:
            return year
    return 1900
movies['year'] = movies['title'].apply(production_year)
ratings_with_movies = pd.merge(ratings, movies[['movieId', 'year']], on='movieId')
average_ratings_by_year = ratings_with_movies.groupby('year')['rating'].mean().reset_index()
average_ratings_by_year_sorted = average_ratings_by_year.sort_values(by='rating', ascending=False)
print(average_ratings_by_year_sorted.head())

plt.figure(figsize=(12, 6))
plt.plot(average_ratings_by_year_sorted['year'], average_ratings_by_year_sorted['rating'], marker='o')
plt.title('Средний рейтинг фильмов по годам выпуска')
plt.xlabel('Год выпуска')
plt.ylabel('Средний рейтинг')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""
Гипотеза H0 год выпуска фильма не влияет на средний рейтинг.
"""
years = average_ratings_by_year_sorted['year']
ratings = average_ratings_by_year_sorted['rating']
X = years.values.reshape(-1, 1)
y = ratings.values

correlation, p_value = linregress(years, ratings)[:2]
print(f"Коэффициент корреляции (R): {correlation}")
print(f"P-значение: {p_value}")

if p_value > 0.05:
    print("Гипотеза подтверждена.")
else:
    print("Гипотеза опровергнута.")