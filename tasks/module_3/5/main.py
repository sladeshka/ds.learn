"""
Задание 1
"""
import json
import csv
purchases_dict = {}
try:
    with open('purchase_log.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                purchase = json.loads(line)
                user_id = purchase['user_id']
                category = purchase['category']
                purchases_dict[user_id] = category
            except json.JSONDecodeError as e:
                print(f"Ошибка разбора строки: {line}\n{str(e)}")
except FileNotFoundError:
    print("Файл не найден.")
    exit(1)

"""
Задание 2
"""
try:
    with open('visit_log.csv', 'r', encoding='utf-8') as infile, open('funnel.csv', 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        try:
            next(reader)
        except StopIteration:
            exit(1)
        writer.writerow(['user_id', 'source', 'category'])

        for row in reader:
            if len(row) < 2:
                print(f"Некорректная строка: {row}")
                continue
            user_id, source = row[0], row[1]
            if user_id in purchases_dict:
                category = purchases_dict[user_id]
                writer.writerow([user_id, source, category])

except FileNotFoundError:
    print("Файл не найден.")
    exit(1)
