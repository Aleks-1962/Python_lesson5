""" Определить, кто из сотрудников имеет оклад менее 20 тыс. и выводим фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

my_fil = open('less5_3.txt', 'r', encoding='utf-8')

name = []
sal_name = []

for num in my_fil.read().split('\n'):
    num = num.split()
    if float(num[1]) < 20000:
        name.append(num[0])
    sal_name.append(num[1])
print(f'Оклад меньше 20000 {name}, средний оклад {sum(map(float, sal_name)) / len(sal_name)}')

my_fil.close()
