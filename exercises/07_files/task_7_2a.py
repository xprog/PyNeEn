# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys

arg = sys.argv[1]



with open(arg) as f:
    for line in f:   
        line = line.rstrip()
        if not line.startswith("!"):
            is_ignore = False
            for ign in ignore:
                if line.find(ign) != -1:
                    is_ignore = True
            if is_ignore == False:
                print(line)
