""" Записываем построчно фамилии сотрудников и их оклады.
Определить, кто из сотрудников имеет оклад менее 20 тыс. и выводим фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

#with open('less5_3.txt', 'w', encoding='utf-8') as f_obj:
#    try:
#        while True:
#            name_f = input('Введите сотрудник - ')
#            float_f = input('Введите оклад сотрудника - ')
#            if len(name_f) != 0: # or len(float_f) == 0
#                f_obj.writelines(name_f + '\t' + str(float_f) + '\n')
#            else:
#                break
#    except IOError:
#        print('Ошибка ввода данных!')

my_fil = open('less5_3.txt', 'r', encoding='utf-8')
# my_list = {}
#my_list = my_fil.readlines()
name = []
sal_name = []
#new_list = [v for i, v in enumerate(my_list) if int(v) < 20]
#print(new_list)
for num in my_fil.read().split('\n'): #range(len(my_list)):
    num = num.split()
    if float(num[1]) < 20000:
        name.append(num[0])
    sal_name.append(num[1])
print(f'Оклад меньше 20000 {name}, средний оклад {sum(map(float, sal_name)) / len(sal_name)}')
#    print(my_list[num], end=" ")
#content = my_fil.read()
#print('Данные введенны пользователем:\n' + content)
my_fil.close()
