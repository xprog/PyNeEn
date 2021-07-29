# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ip_and_mask = argv[1]

# ip_and_mask = input("вводите IP-сети в формате 10.1.1.0/24 :")
# ip_and_mask = "10.1.1.1/24"

ip, mask  = ip_and_mask.split("/")[0], int(ip_and_mask.split("/")[1])

ip_octets_str = ip.split(".")
ip_octets = [int(ip_octets_str[0]), int(ip_octets_str[1]), int(ip_octets_str[2]), int(ip_octets_str[3])]

mask_bit = "{:<032}".format("1" * mask)

net_template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}'''

mask1_bin = mask_bit[0:8]
mask2_bin = mask_bit[8:16]
mask3_bin = mask_bit[16:24]
mask4_bin = mask_bit[24:]

ip_octets[0] = ip_octets[0] &  int(mask1_bin, 2)
ip_octets[1] = ip_octets[1] &  int(mask2_bin, 2)
ip_octets[2] = ip_octets[2] &  int(mask3_bin, 2)
ip_octets[3] = ip_octets[3] &  int(mask4_bin, 2)


print(net_template.format(ip_octets[0], ip_octets[1], ip_octets[2], ip_octets[3]))

print(f"\nMask:\n"
    f"{int(mask1_bin, 2):<10}{int(mask2_bin, 2):<10}{int(mask3_bin, 2):<10}{int(mask4_bin, 2):<10}\n"
    f"{mask1_bin:10}{mask2_bin:10}{mask3_bin:10}{mask4_bin:10}")
