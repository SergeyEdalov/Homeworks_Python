# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1.Программа должна выводить данные 
# 2.Программа должна сохранять данные в текстовом файле 
# 3.Пользователь может ввести одну из характеристик для поиска определенной 
# записи(Например имя или фамилию человека) 4.Использование функций. 
# Ваша программа не должна быть линейной

# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать телефонную книгу
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

path = 'fhone_book.txt'

# 1. Открыть файл
def open_phonebook():
    data = open(path, 'a', encoding='UTF-8')

# open_textbook()

# 2. Сохранить файл
def save_phonebook():
    data = open(path, 'a', encoding='UTF-8')
    data.close()

# save_textbook()

# 3. Показать телефонную книгу

def show_phonebook():
    data = open(path, 'r', encoding='UTF-8')
    print(data.read())
    data.close()

# show_phonebook()

# 4. Добавить контакт
def add_contact():
    data = open(path, 'a', encoding='UTF-8')
    name = input('Введите имя контакта: ').capitalize()
    mid_name = input('Введите отчество контакта: ').capitalize()
    last_name = input('Введите фамилию контакта: ').capitalize()
    phone_number = input('Введите номер телефона: ').capitalize()
    data.write(f'{name} {mid_name} {last_name} {phone_number}')
    data.close()


# add_contact()

# 5. Найти контакт
def find_contact():
    data = open(path, 'r', encoding='UTF-8')
    find_contact = input('Какой контакт вы хотите найти?: ')
    text = data.readlines()
    for i in text:
        i_1 = i.strip().split(' ')
        if i_1[0] == find_contact or i_1[1] == find_contact or i_1[2] == find_contact or i_1[3] == find_contact:
            print(i)
            break   
    else: print('Такого контакта нет в телефонной книге')

# find_contact()


# 6. Изменить контакт

def change_contact():
    data = open(path, 'r+', encoding='UTF-8')
    changed_contact = input('Введите измененяемый контакт: ')
    text = data.readlines()
    new_contact = input('Введите замену: ')
    for contact in text:
        if contact == changed_contact:
            changed_contact = new_contact
    return text

# print(change_contact())

# 7. Удалить контакт

def delete_contact():
    data = open(path, 'r+', encoding='UTF-8')
    deleted_contact = input('Введите удаляемый контакт: ')
    text = data.readlines()
    for contact in text:
        if contact == deleted_contact:
            text.remove(deleted_contact)
    return text

# delete_contact()

# 8. Выход
def exit():
    data = open(path, 'a', encoding='UTF-8')
    data.close()




greetings = 'Здравствуй, дорогой пользователь. Чем я могу вам помочь?'
print(greetings)
menu = {1:'открыть телефонную книгу', 2:'сохранить телефонную книгу', 3:'показать телефонную книгу', 4:'добавить контакт',
         5:'найти контакт', 6:'изменить контакт', 7:'удалить контакт', 8:'выход'}

for key, value in menu.items():
    print(f"{key}  - {value}")

def menu(x):
    while x != 8:
        if x == 1: open_phonebook()
        elif x == 2: save_phonebook()
        elif x == 3: show_phonebook()
        elif x == 4: add_contact()
        elif x == 5: find_contact()
        elif x == 6: change_contact()
        elif x == 7: delete_contact()
        else: print('Такого пункта нет в меню. Выберите пункт от 1 до 8')
menu(int(input()))

    
