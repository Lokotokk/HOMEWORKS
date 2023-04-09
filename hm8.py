''' Задача №49. Решение в группах
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи
(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''
'''
Домащнее задание.
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных.
'''


def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book1.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    """Добавляет информацию в справочник"""
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book1.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Успешно!')


def find_data() -> None:
    """осуществляет поиск по справочнику"""
    data = input('Введите данные для поиска: ')
    with open('book1.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    return search(tel_book, data)


def search(book: str, info: str) -> str:
    """находит в строке записи по определенному критерию поиска"""
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def change_data() -> None:
    """вносит изменения в справочник"""
    with open('book1.txt', 'r', encoding='utf-8') as f:
        all_items = f.read().split('\n')
        searh_for_change = find_data()
        print(all_items[all_items.index(searh_for_change)])
        if all_items[all_items.index(searh_for_change)] == '':
             print('Информация не найдена')
             return 0
        all_items[all_items.index(searh_for_change)] = input('Введите новые данные (ФИО | тел.) : ')
    with open('book1.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_items))
        print('Изменения внесены')


while True:
    print('1.вывод, 2.добавление, 3.поиск, 4.внести изменения')
    mode = int(input())
    if mode == 1:
        show_data()
    elif mode == 2:
        add_data()
    elif mode == 3:
        find_data()
    elif mode == 4:
        change_data()
    else:
        break
