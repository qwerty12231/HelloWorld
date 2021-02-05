"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import math

subj = {}

with open("file_6.txt", "r", encoding="utf-8") as init_f:
    for line in init_f:
        line = line.replace("-", "0").replace(":", "").replace("lecture","").replace("practice","").replace("lab","").split()
        subj[line[0]] = sum(map(int, line[1:]))
    print(f'Общее количество часов по предмету - \n {subj}')
# В общем так и не работает эта задача, хотя ее уже сделала по Вашей рек.(