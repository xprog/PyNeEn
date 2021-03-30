# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open("ospf.txt") as f:
    for line in f:   
        st = line.replace(",", "").split()
#        print(st)

#        for s in st:
#            print(s)
#        print("-"*50)

        template = "{:<22}{}\n{:<22}{}\n{:<22}{}\n{:<22}{}\n{:<22}{}"

        print(template.format("Prefix", st[1], "AD/Metric", st[2][1:-1], \
        "Next-Hop", st[4], "Last update", st[5], "Outbound Interface", st[6]))
#        print("-"*50)
    

