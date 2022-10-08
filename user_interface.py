import operation as op
import check as ch


def get_menu_item(n):
    '''
    Получение пункта меню от пользователя
    где n - количество пунктов в меню
    '''
    return ch.number_menu('выберете пункт меню: ', n)

 
def convert_type_telefon(number):
    '''
    Конвертация типа телефона из числа [1, 6] 
        в строку (сотовый, городской, домашний, рабочий, личный, другой)
    '''
    if number == 1: return 'сотовый'
    if number == 2: return 'городской'
    if number == 3: return 'домашний'
    if number == 4: return 'рабочий'
    if number == 5: return 'личный'
    if number == 6: return 'другой'


def get_name_contact(string):
    '''
    Получение имени или фамилии или отчества 
        или комментария контакта от пользователя
    '''
    return ch.check_name_contact(string)


def get_number_telefon(string):
    '''
    Получение номера телефона от пользователя
    '''
    return ch.check_number_telefon(string)


def add_contact(contact):
    '''
    Добавление контакта в телефонную книгу
    '''
    return op.add_contact(contact)


def find_contact_index(string):
    '''
    Поиск индекса контакта
    '''
    return op.contact_search(string)


def delete_contact(index):
    '''
    Удаление контакта по инддексу
    '''
    return op.del_contact(index)
