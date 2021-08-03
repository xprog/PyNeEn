# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status



london_co = {
'r1' : {
'hostname': 'london_r1',
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'IOS': '15.4',
'IP': '10.255.0.1'
},
'r2' : {
'hostname': 'london_r2',
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'IOS': '15.4',
'IP': '10.255.0.2'
},
'sw1' : {
'hostname': 'london_sw1',
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '3850',
'IOS': '3.6.XE',
'IP': '10.255.0.101'
}
}

def convert_config_to_dict(config_filename):
    result = {}
    with open(config_filename) as file:
        key, key_last = None, None
        command = []
        for line in file:
            if not line.startswith("!") and line.strip() and not ignore_command(line, ignore):
                if not line.strip("\n").startswith(" "):
                    key_last = key
                    key = line.strip()
                    if key_last:
                        result[key_last] = command
                        command = []
                        # print(key_last, result[key_last])
                else:
                    command.append(line.strip())

    result[key] = command
    # print(key, result[key])

    return result

result = convert_config_to_dict("config_sw1.txt")

print(result)