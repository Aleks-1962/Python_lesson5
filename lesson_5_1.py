"""Создание программно файл в текстовом формате,
 запись в него построчно данные, вводимые пользователем.
 Окончание ввода данных пустая строка."""

with open('less5_1.txt', 'w') as f_obj:
    try:
        while True:
            str_f = input('Введите данные для записи в файл - \n')
            f_obj.writelines(str_f+'\n')
            if len(str_f) == 0:
                break
    except IOError:
        print('Ошибка ввода данных!')

my_fil = open('less5_1.txt', 'r')
content = my_fil.read()
print('Данные введенные пользователем:\n' + content)
my_fil.close()