import pandas as pd
"""
Задание 1

Для датафрейма log из материалов занятия создайте столбец source_type по правилам:

* если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
* для источников paid и email из России ставим ad;
* для источников paid и email не из России ставим other;
* все остальные варианты берём из traffic_source без изменений.
"""
log = pd.read_csv('visit_log.csv', delimiter=';')
def determine_source_type(row):
    if row['traffic_source'].lower() in ['yandex', 'google']:
        return 'organic'
    elif row['traffic_source'].lower() in ['paid', 'email'] and row['region'].lower() == 'russia':
        return 'ad'
    elif row['traffic_source'].lower() in ['paid', 'email'] and row['region'].lower() != 'russia':
        return 'other'
    else:
        return row['traffic_source']
log['source_type'] = log.apply(determine_source_type, axis=1)
print(log.head())
"""
Задание 2

В файле URLs.txt содержатся URL страниц новостного сайта. Вам нужно отфильтровать его по адресам страниц с текстами новостей. Известно, что шаблон страницы новостей имеет внутри URL конструкцию: /, затем 8 цифр, затем дефис. Выполните действия:

1. Прочитайте содержимое файла с датафрейм.
2. Отфильтруйте страницы с текстом новостей, используя метод str.contains и регулярное выражение в соответствие с заданным шаблоном.
"""
urls_df = pd.DataFrame({'url': pd.read_csv('URLs.txt', header=None)[0]})
news_urls = urls_df[urls_df['url'].str.contains(r'/\d{8}-')]
print(news_urls.head())
"""
Задание 3

Используйте файл с оценками фильмов ratings.csv. Посчитайте среднее время жизни пользователей, которые выставили более 100 оценок. Под временем жизни понимается разница между максимальным и минимальным значениями столбца timestamp для данного значения userId.
"""
ratings = pd.read_csv('ratings.csv')
user_counts = ratings['userId'].value_counts()
active_user_ids = user_counts[user_counts > 100].index
active_ratings = ratings[ratings['userId'].isin(active_user_ids)]
user_lifetime = active_ratings.groupby('userId')['timestamp'].agg(['max', 'min']).reset_index()
user_lifetime.columns = ['userId', 'max_timestamp', 'min_timestamp']
user_lifetime['lifetime'] = user_lifetime['max_timestamp'] - user_lifetime['min_timestamp']
average_user_lifetime = user_lifetime['lifetime'].mean()
print(average_user_lifetime)

"""
Задание 4
Дана статистика услуг перевозок клиентов компании по типам (см. файл “Python_13_join.ipynb” в разделе «Материалы для лекции “Продвинутый pandas”» ---- Ноутбуки к лекции «Продвинутый pandas»).
Нужно сформировать две таблицы:

* таблицу с тремя типами выручки для каждого client_id без указания адреса клиента;
* аналогичную таблицу по типам выручки с указанием адреса клиента.
Обратите внимание, что в процессе объединения таблиц данные не должны теряться.
"""
rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)
revenue_without_address = pd.merge(rzd, auto, on='client_id', how='outer')
revenue_without_address = pd.merge(revenue_without_address, air, on='client_id', how='outer')
revenue_with_address = pd.merge(revenue_without_address, client_base, on='client_id', how='outer')

print(revenue_without_address)

print(revenue_with_address)