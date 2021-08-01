# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_access_config(intf_vlan_mapping, access_template):

    result = {}
    for intf, vlans in intf_vlan_mapping.items():
        result[intf] = None
        # result.append(f"interface {intf}")
        commands = []
        for command in access_template:
            if command.endswith("vlan"):

                vlan = ""
                for v in vlans:
                    vlan = f"{vlan},{v}"

                commands.append(f'{command} {vlan.lstrip(",")}')
                # result[intf] = f'{command} {vlan.lstrip(",")}'
            else:
                # result.append(f"{command}")
                commands.append(f'{command}')

        result[intf] = commands
    return result

result = generate_access_config(trunk_config, trunk_mode_template)

# for key, value in result.items():
#     print(key, value)

print(result)
