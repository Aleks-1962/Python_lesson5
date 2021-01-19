""" Выполняем подсчет строк и слов каждой строчке файла. Файл заранее создан"""
with open('less5_2.txt', 'r', encoding='utf-8') as f_r:
    lines = f_r.readlines()
    print(type(lines))
    num_lines = len([l for l in lines])
    print('Количество строк в файле - '+ str(num_lines))
my_file = open('less5_2.txt', 'r', encoding='utf-8')

content = my_file.readlines()

for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('less5_2.txt', 'r', encoding='utf-8')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

