""" Открываем файл на чтение и считываем данные построчно.
Английские числительные заменяем на русские. Новые данные записываем в новый текстовый файл."""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_f = []
with open('less5_4.txt', 'r') as f_r:
    for num in f_r:
        num = num.split(' ', 1)
        print(num)
        new_f.append(rus[num[0]] + '  ' + num[1])
    print(new_f)

with open('new_less5_4.txt', 'w', encoding='utf-8') as f_w:
    f_w.writelines(new_f)


# C  "from googletrans import Translator" не заработало
#
#
# translator = Translator()
# rez = translator.translator('fox', dest='ru')
