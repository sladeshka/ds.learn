"""
Задание 1
"""

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    "1": ["2207 876234", "11-2"],
    "2": ["10006"],
    "3": []
}

def run_command_line():
    document_not_found = "Документ не найден в базе"
    while True:
        command = input("Введите команду: ")
        current_directories = "Текущий перечень полок:" + ", ".join(directories.keys())
        if command == 'q':
            break
        elif command == 'p':
            owner = find_owner_by_document_number(input("Введите номер документа: "))
            if owner:
                print(f"Владелец документа: {owner}.")
            else:
                print(document_not_found)
        elif command == 's':
            directory = find_directory_by_document_number(input("Введите номер документа: "))
            if directory:
                print(f"Документ хранится на полке: {directory}.")
            else:
                print(document_not_found)
        elif command == 'l':
            print(format_documents())
        elif command == 'ads':
            number = input("Введите номер полки: ")
            if add_directory(number):
                current_directories = "Текущий перечень полок:" + ", ".join(directories.keys())
                print(f"Полка добавлена. " + current_directories)
            else:
                print(f"Такая полка уже существует. " + current_directories)
        elif command == 'ds':
            number = input("Введите номер полки: ")
            if there_is_directory(number):
                if delete_directory(number):
                    current_directories = "Текущий перечень полок:" + ", ".join(directories.keys())
                    print(f"Полка удалена. " + current_directories)
                else:
                    print(f"На полке есть документы, удалите их перед удалением полки. " + current_directories)
            else:
                print(f"Такой полки не существует. " + current_directories)
        else:
            print("Нет такой команды")

"""
Пункт 1. 

Пользователь по команде «p» может узнать владельца документа по его номеру.
Примеры работы:
Введите команду:
"""
def find_owner_by_document_number(doc_number):
    for document in documents:
        if document['number'] == doc_number:
            return document['name']
    return None
run_command_line()
""""
Введите команду:
p
Введите номер документа:
10006
Введите команду:
q
Результат:
Владелец документа: Аристарх Павлов
"""
run_command_line()
"""
Введите команду:
p
Введите номер документа:
12345
Введите команду:
q
Результат:
Документ не найден в базе
"""

"""
Пункт 2. 

Пользователь по команде «s» может по номеру документа узнать, на какой полке он хранится.
Примеры работы:
"""
def find_directory_by_document_number(document_number):
    for directory, docs in directories.items():
        if document_number in docs:
            return directory
    return None
run_command_line()
"""
Введите команду:
s
Введите номер документа:
10006
Введите команду:
q
Результат:
Документ хранится на полке: 2
"""
run_command_line()
"""
Введите команду:
s
Введите номер документа:
12345
Введите команду:
q
Результат:
Документ не найден в базе
"""

"""
Пункт 3. 

Пользователь по команде «l» может увидеть полную информацию по всем документам.
Пример работы:
"""
def format_documents():
    result = []
    for document in documents:
        directory = find_directory_by_document_number(document["number"])
        result.append(f"№: {document['number']}, тип: {document['type']}, владелец: {document['name']}, полка хранения: {directory if directory else 'Нет'}")
    return "\n".join(result)
run_command_line()
"""
Введите команду:
l
Введите команду:
q
Результат:
№: 2207 876234, тип: passport, владелец: Василий Гупкин, полка хранения: 1
№: 11-2, тип: invoice, владелец: Геннадий Покемонов, полка хранения: 1
№: 10006, тип: insurance, владелец: Аристарх Павлов, полка хранения: 2
"""

"""
Пункт 4. 

Пользователь по команде «ads» может добавить новую полку.
Примеры работы:
"""
def add_directory(number):
    if number not in directories:
        directories[number] = []
        return True
    return False
run_command_line()
"""
Введите команду:
ads
Введите номер полки:
10
Введите команду:
q
Результат:
Полка добавлена. Текущий перечень полок: 1, 2, 3, 10.
"""
run_command_line()
"""
Введите команду:
ads
Введите номер полки:
1
Введите команду:
q
Результат:
Такая полка уже существует. Текущий перечень полок: 1, 2, 3.
"""

"""
Пункт 5. 

Пользователь по команде «ds» может удалить существующую полку из данных, только если она пустая.
Примеры работы:
"""
def there_is_directory(number):
    if number in directories:
        return True
    return False

def directory_is_empty(number):
    if len(directories[number]) == 0:
        return True
    return False
def delete_directory(number):
    if there_is_directory(number) and directory_is_empty(number):
        del directories[number]
        return True
    return False
run_command_line()
"""
Введите команду:
ds
Введите номер полки:
3
Введите команду:
q
Результат:
Полка удалена. Текущий перечень полок: 1, 2
"""
run_command_line()
"""
Введите команду:
ds
Введите номер полки:
1
Введите команду:
q
Результат:
На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: 1, 2, 3.
"""
run_command_line()
"""
Введите команду:
ds
Введите номер полки:
4
Введите команду:
q
Результат:
Такой полки не существует. Текущий перечень полок: 1, 2, 3.
"""