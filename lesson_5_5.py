""" Создаем файл, записываем в него числа. Подсчет суммы чисел"""

with open('less5_5.txt', 'w+') as f_obj:
    try:
        str_f = input('Введите числа через пробел для записи в файл - \n')
        f_obj.writelines(str_f+'\n')
        s = sum(map(float, str_f.split()))
        print('Сумма введенных чисел - ' + str(s))
    except IOError:
        print('Ошибка ввода данных!')
