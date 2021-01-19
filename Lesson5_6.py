""" Создать словарь с содержанием: предмет и количество часов. Вывести его на экран"""
less = {}

with open('less5_6.txt', 'r', encoding='utf-8') as f_r:
    for line in f_r:
        print(line)
        lesson, lec, pr, lab = line.split()
        lec = "".join(filter(str.isnumeric, lec))
        pr = "".join(filter(str.isnumeric, pr))
        lab = "".join(filter(str.isnumeric, lab))
        if len(lec) !=0:
           lec1 = int(lec)
        else:
            lec1 = 0
        if len(pr) != 0:
            pr1 = int(pr)
        else:
            pr1 = 0
        if len(lab) != 0:
           lab1 = int(lab)
        else:
            lab1 = 0
        rez = lec1 + pr1 + lab1
        less[lesson] = str(rez)
    print(f'Общее количество часов по предмету -  {less}')

