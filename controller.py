from re import L
import operation as op
import user_interface as ui
import linecache as lin  # доступ к текстовым строкам
import logger as log


def button_click():
    while True:
        op.output_menu_console('S8_tel_menu_start.txt')  # вывод главного меню в консоль
        num_menu_1 = ui.get_menu_item(1)  # запрос пункта меню у пользователя
        log.logging.info('пользователь выбрал в S8_tel_menu_start: ' + str(num_menu_1))

        if num_menu_1 == 1:  # вывод всех контактов в консоль
            op.output_list_contacts_console() 
            log.logging.info('Вывод всех контактов (S8_tel_contact.csv) в консоль')  
            input('для продолжения работы нажмите: "enter"')
            

        if num_menu_1 == 2:  # добавление контакта в телефонную книгу
            '''
            блок получения данных от пользователя и добавление в сипсок
            '''
            list_contact = []  # список для пунктов контакта

            name = ui.get_name_contact('введите имя: ')
            list_contact.append(name)
            patronymic = ui.get_name_contact('введите отчество: ')
            list_contact.append(patronymic)
            surname = ui.get_name_contact('введите фамилию: ')
            list_contact.append(surname)
            op.output_menu_console('S8_tel_type_telefon.txt')  # вывод меню типа телефонов в консоль
            num_menu_2 = ui.get_menu_item(2)  # запрос пункта меню у пользователя
            num_menu_2 = ui.convert_type_telefon(num_menu_2)  # конвертация типа телефона
            list_contact.append(num_menu_2)
            num_tel = ui.get_number_telefon('введите номер телефона: ')
            list_contact.append(num_tel)
            comment = ui.get_name_contact('введите комментарий: ')
            list_contact.append(comment)
            
            ui.add_contact(list_contact)  # запись данных контакта в файл
            log.logging.info('пользователь добавил контакт в S8_tel_contact.csv: ' + str(list_contact))


        if num_menu_1 == 3:  # поиск записи
            find_name = ui.get_name_contact('введите поисковое слово (например имя контакта): ')
            contact_index = ui.find_contact_index(find_name)
            if contact_index == None:  # контакт отсутствует в тел.книге
                input('для продолжения работы нажмите: "enter"')
                continue
            elif contact_index >= 0:  # контакт найден
                print(lin.getline('S8_tel_contacts.csv', contact_index + 1))  # вывод в консоль удаляемого контакта из файла (по индексу строки)
                input('для продолжения работы нажмите: "enter"')
            log.logging.info('Пользователь искал контакт: ' + str(find_name))

        if num_menu_1 == 4:  # удаление записи
            find_name = ui.get_name_contact('введите поисковое слово (например имя контакта): ')
            contact_index = ui.find_contact_index(find_name)  # индекс искомого контакта (либо None при отсутствии)
            if contact_index == None:  # контакт отсутствует в тел.книге
                input('для продолжения работы нажмите: "enter"')
                continue
            elif contact_index >= 0:  # контакт найден
                op.output_menu_console('S8_tel_delete_contact.txt')  # вывод меню "удаление" в консоль
                print(lin.getline('S8_tel_contacts.csv', contact_index + 1))  # вывод в консоль удаляемого контакта из файла (по индексу строки)
                num_menu_3 = ui.get_menu_item(3)
                log.logging.info('пользователь выбрал в S8_tel_delete_contact: ' + str(num_menu_3))
                if num_menu_3 == 2:  # удаление контакта по индексу
                    ui.delete_contact(contact_index)
                    print('контакт удалён!')
                    log.logging.info('Пользователь удалил контакт с индексом: ' + str(contact_index))
                    input('для продолжения работы нажмите: "enter"')
                elif num_menu_3 == 1:  # отмена: не удалять контакт
                    print('удаление контакта отменено!')
                    input('для продолжения работы нажмите: "enter"')

        if num_menu_1 == 5:  # выход из программы
            log.logging.info('Пользователь вышел из программы')
            return False 

#button_click()