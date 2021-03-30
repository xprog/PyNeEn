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

vlans = {}

with open("CAM_table.txt") as file_src:
    for str_conf in file_src:
#        print(str_conf)
        if "DYNAMIC" in str_conf:
            vlan, mac, _, port = str_conf.split()
            current_str = "{:<9}{:<20}{}".format(vlan, mac, port)
            #print(current_str)

            # храним данные в таком формате:
            #[vlan1: (sett1, sett2, ..), vlan2: (sett1, sett2, ..), ..]
            
            if int(vlan) not in vlans.keys():
                vlans[int(vlan)] = []
               
            vlans[int(vlan)].append(current_str)

vlans_sorted = sorted(vlans)

vlan_number = int(input("введите номер VLANа;"))


for vl in vlans_sorted:
    if vl == vlan_number:
        for vl in vlans[vl]:
            print(vl)
