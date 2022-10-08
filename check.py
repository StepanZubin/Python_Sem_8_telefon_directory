def number_menu(string, n) -> int:
    '''
    Метод: Выбор пункта меню.
    Аргумент: Строка для пользователя, Число выбора диапазона меню.
    Возвращаемое значение: Число в интервале диапазона меню.
    '''
    try:
        num = int(input(string))
        if n == 1:
            if num < 1 or num > 5:
                print('некорректный ввод!')
                return number_menu(string, n)
        elif n == 2:
            if num < 1 or num > 6:
                print('некорректный ввод!')
                return number_menu(string, n) 
        elif n == 3:
            if num < 1 or num > 2:
                print('некорректный ввод!')
                return number_menu(string, n) 
        return num
    except ValueError:
        print('некорректный ввод!')
        return number_menu(string, n)


def check_name_contact(string):
    '''
    Метод: Пользовательский ввод имени. 
        Проверка на корректность ввода строки буквенных символов.
    Аргумент: Строка пояснения пользователю.
    Возвращаемое значение: Строка с именем.
    '''
    name = input(string)

    if len(name) > 15:
        print('недопустимое количество символов!')
        return check_name_contact(string)
    elif len(name) == 0:
        print('вы ввели пустую строку!')
        return check_name_contact(string)
    elif name.isalpha(): return name.title() 
    # .title() - преобразования первого символа в слове в верхний регистр
    else: 
        print('некорректный ввод!')
        return check_name_contact(string) 


def check_number_telefon(string):
    '''
    Метод: Пользовательский ввод номера телефона.
        Проверка корректности ввода
    Аргумент: Строка пояснения пользователю.
    Возвращаемое значение: Номер телефона.
    '''
    try:
        num_N = input(string)
        if len(num_N) > 11 or len(num_N) < 5: 
            print('некорректный ввод!')
            return check_number_telefon(string)
        num_tel = int(num_N)
        return(num_tel)
    except ValueError:
        print('некорректный ввод!')
        return check_number_telefon(string)
    
    