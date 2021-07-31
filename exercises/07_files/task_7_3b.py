# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["ddress", "---"]
config_result = []

vlan = int(input("вводи номера VLAN:  "))

filename = "CAM_table.txt"
with open(filename) as file:
    for f in file:
        if not f.startswith("!"):
            is_ignore = False
            for ign in ignore:
                if ign in f:
                    is_ignore = True

            if not is_ignore and f.strip():
                current = []
                config = f.strip().split()

                current = [int(config[0]), config[1], config[3]]

                # запоминать информацию только по указанному VLAN
                if current[0] == vlan:
                    config_result.append(current)

config_result.sort()

for cr in config_result:
    print("{:<9}{:<20}{:}".format(cr[0], cr[1], cr[2]))