# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("введите IP-сети в формате: 10.1.1.0/24: ")

# ip = "10.5.5.0/24"

ip_and_mask = ip.split("/")

ip = ip_and_mask[0]
mask = ip_and_mask[1]
ip = ip.split(".")

template = '''Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:>08b}  {1:>008b}  {2:>08b}  {3:>08b}


Mask:
/{4}
{5:<8}  {6:<8}  {7:<8}  {8:<8}
{9:<8}  {10:<8}  {11:<8}  {12:<8}'''

template_mask_0 = "{:<032}"

mask = int(mask)
mask_dec = mask
mask = "1"*mask
mask = template_mask_0.format(mask)

mask1_bin = mask[0:8]
mask2_bin = mask[8:16]
mask3_bin = mask[16:24]
mask4_bin = mask[24:]

print(template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]), \
                      mask_dec, \
                      int(mask1_bin, 2), int(mask2_bin, 2), int(mask3_bin, 2), int(mask4_bin, 2), \
                      mask1_bin, mask2_bin, mask3_bin, mask4_bin))