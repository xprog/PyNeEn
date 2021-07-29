# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_correct = False

while not ip_correct:

    ip = input("Введите IP-адрес в формате 10.0.1.1: \n")
    # ip = "10,0.1.1.5"

    ip_correct = True

    # ip_octet = int(ip.split(".")[0])
    ip_octets = ip.split(".")

    # состоит из 4 cимволов,разделенных "."
    if len(ip_octets) != 4:
        ip_correct = False

    for oct_str in ip_octets:

        if ip_correct == False:
            break

        if not oct_str.isdigit():
            ip_correct = False
            break
        elif int(oct_str) < 0 or int(oct_str) > 255:
            ip_correct = False
            break

    if ip_correct != False:

        if ip_octets[0].isdigit():
            ip_octet = int(ip_octets[0])
        else:
            ip_correct = False

    if ip_correct == False:
        text = 'Неправильный IP-адрес'
    elif ip == "0.0.0.0":
        text = 'unassigned'
    elif ip_octet >= 0 and ip_octet <= 223:
        text = 'unicast'
    elif ip_octet >= 224 and ip_octet <= 239:
        text = 'multicast'
    elif ip  == "255.255.255.255":
        text = 'local broadcast'
    else:
        text = 'unused'

    print(text)
