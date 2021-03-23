# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

text = "first"

if text != "":
    ip = input("Введите IP-адреса в формате 10.0.1.1: ")

    #ip = "10.0.1.1"
    #ip = "255.255.255.255"
    #ip = "0.0.0.0"


    ips = ip.split(".")

    text = ""


    if ip.count(".") != 3:
        text = "Неправильный IP-адрес"
    elif ips[0].isdigit() == False or ips[1].isdigit() == False or \
    ips[2].isdigit() == False or ips[3].isdigit() == False:
        text = "Неправильный IP-адрес"
    else:
        for i in ips:
            if int(i) <0 or int(i) > 255:
                text = "Неправильный IP-адрес"


#print(ips)

if text != "Неправильный IP-адрес":

    if int(ips[0]) >= 1 and int(ips[0]) <= 223:
        text = "unicast"
    elif int(ips[0]) >= 224 and int(ips[0]) <= 239:
        text = "multicast"
    elif ip == "255.255.255.255":
        text = "local broadcast"
    elif ip == "0.0.0.0":
        text = "unassigned"
    else:
        text = "unused"

print(text)
