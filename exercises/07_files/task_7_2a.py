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

from sys import argv

# filename = "config_sw1.txt"
# with open(filename) as file:
with open(argv[1]) as file:
    for f in file:
        if not f.startswith("!"):
            is_ignore = False
            for ign in ignore:
                if ign in f:
                    is_ignore = True

            if not is_ignore:
                print(f.rstrip())
