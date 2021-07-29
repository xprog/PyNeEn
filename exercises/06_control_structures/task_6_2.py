# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("Введите IP-адрес в формате 10.0.1.1")
# ip = "10.0.1.1"

ip_octet = int(ip.split(".")[0])

if ip == "0.0.0.0":
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