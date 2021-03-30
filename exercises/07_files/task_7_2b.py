# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys

src = sys.argv[1]
dst = sys.argv[2]


with open(src) as f_src, open(dst, "w") as f_dst:
    for line in f_src:   
        line = line.rstrip()
        if not line.startswith("!"):
            is_ignore = False
            for ign in ignore:              
                if line.find(ign) != -1:
                    is_ignore = True
            if is_ignore == False:
                f_dst.write(line + "\n")
#                print(line)
