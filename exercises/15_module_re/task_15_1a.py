# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re

def get_ip_from_cfg(filename):
    result = {}
    template_intf = r"^interface (\S+)"
    template = r"address ((\d+\.?){4}) ((\d+.?){4})"

    with open(filename) as file:
        for f in file:
            # line = f.write()
            ip = re.search(template, f)
            intf = re.search(template_intf, f)
            if intf:
                interface = intf.group(1)
                # print(interface)
                # print(">>>>  ", f)
            if ip:
                result[interface] = (ip.group(1), ip.group(3))
                # print(interface)
                # print(ip.group(), "===", ip.group(1), ip.group(3))

    return result

if __name__ == "__main__":
    get_ip_from_cfg("config_r1.txt")