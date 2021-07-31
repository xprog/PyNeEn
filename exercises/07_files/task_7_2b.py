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

from sys import argv

# filename = "config_sw1.txt"
# with open(filename) as file:
with open(argv[1]) as file_src, open(argv[2], "w") as file_dst:
    for f in file_src:
        if not f.startswith("!"):
            is_ignore = False
            for ign in ignore:
                if ign in f:
                    is_ignore = True

            if not is_ignore:
                file_dst.writelines(f)
                # print(f.rstrip())