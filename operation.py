import csv
import os


def output_menu_console(string):
    '''
    Метод: Вывод меню в консоль
    Аргумент: Название текстового файла в директории
    '''
    os.system('cls')
    with open(string, 'r', encoding='utf-8') as txtfile:
        for line in txtfile:
            print(line.rstrip())


def output_list_contacts_console():
    '''
    Метод: Вывод списка контактов в консоль
    '''
    os.system('cls')
    with open('S8_tel_contacts.csv', 'r', encoding='utf-8') as csvfile:
        print('  СПИСОК КОНТАКТОВ: ')
        print(csvfile.read())
        

def add_contact(contact):
    '''
    Метод: Добавления строки с контактом в файл csv.
    '''
    with open('S8_tel_contacts.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter= ',')
        writer.writerow(contact)


def del_contact(index):
    '''
    Метод: Удаление строки с контактом в файле csv.
    ''' 
    with open("S8_tel_contacts.csv","r", encoding='utf-8') as file:
        lines = file.readlines()
    del lines[index]  # индекс удаляемой строки
    with open("S8_tel_contacts.csv","w", encoding='utf-8') as file:
        file.writelines(lines)


def contact_search(data):
    '''
    Метод: Поиск контакта.
    '''
    line = []
    count = 0
    try:
        open('S8_tel_contacts.csv')
        with open('S8_tel_contacts.csv', encoding='utf-8') as csvfile:
            file_reader = list(csv.reader(csvfile, delimiter=','))
            for row in file_reader:
                if data.capitalize() in row:
                    '''
                    .capitalize() преобразует первый символ строки в верхний регистр 
                        и переводит в нижний регистр все остальные символы, если таковые имеются.
                    '''
                    count += 1
                    line.append(row)  # добавление строки в список 
                    index = file_reader.index(row)  # индекс строки с искомым контактом
                    #print(row)
            if count == 0:
                print('контакт не найден')
                return None
    except FileNotFoundError:
        print('в телефонной книге нет контактов!')
    return index
