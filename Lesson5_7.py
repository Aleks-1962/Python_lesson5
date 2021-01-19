

import json
profit = {}
pr = {}
prof = 0
i = 0
with open('less5_7.txt', 'r', encoding='utf-8') as f_r:
    for line in f_r:
        name, firm, prof_f, cost_f = line.split()
        profit[name] = int(prof_f) - int(cost_f)
        if profit.get(name) >= 0:
            prof = prof + profit.get(name)
            i += 1
    if i != 0:
        prof_aver = prof/i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутствует. Фирмы работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой Фирмы - {profit}')

with open('less5_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit, indent=4, ensure_ascii=False,)
    print(f'Файл с расширением json - \n ' f' {js_str}')
