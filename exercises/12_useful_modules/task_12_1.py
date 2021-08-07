# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


import subprocess

def ping_ip_addresses(ip_list):
    ip_online = []
    ip_offline = []

    for ip in ip_list:
        result = subprocess.run(['ping', '-n', '1', ip],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='UTF-8')
        if result.returncode == 0:
            ip_online.append(ip)
            # print(result.returncode, result.stdout)
        else:
            ip_offline.append(ip)
            # print(result.returncode, result.stdout)

    # print("xx", ip_online, ip_offline)
    return ip_online, ip_offline


if __name__ == "__main__":
    list_of_ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    # ip_online, ip_offline = ping_ip_addresses(list_of_ips)
    ping_ip_addresses(list_of_ips)
    # print(ip_online, ip_offline)