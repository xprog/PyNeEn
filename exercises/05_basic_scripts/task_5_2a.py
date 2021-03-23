# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = input("введите IP-сети в формате: 10.1.1.0/24\n")

ip_and_mask = ip.split("/")
ip = ip_and_mask[0]
mask = ip_and_mask[1]

ip = ip_and_mask[0]
mask = ip_and_mask[1]

#ip = "11.22.33.44"
#mask = "23"

ip = ip.split(".")

#print(ip, mask)

template_mask_0 = "{:<032}"
mask = int(mask)
mask_dec = mask
mask = "1"*mask
mask = template_mask_0.format(mask)

mask1_bin = mask[0:8]
mask2_bin = mask[8:16]
mask3_bin = mask[16:24]
mask4_bin = mask[24:]


template_ip_dec = "{:<8} {:<8} {:<8} {:<8}"
template_ip_bin = "{0:>08b} {1:>008b} {2:>08b} {3:>08b}"

ip[0] = int(ip[0]) & int(mask1_bin, 2)
ip[1] = int(ip[1]) & int(mask2_bin, 2)
ip[2] = int(ip[2]) & int(mask3_bin, 2)
ip[3] = int(ip[3]) & int(mask4_bin, 2)



print("Network:")
print(template_ip_dec.format(ip[0], ip[1], ip[2], ip[3]))
print(template_ip_bin.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))

template_mask_1 = "\nMask:\n/{}"
template_mask_bin = "{:>08} {:>08} {:>08} {:>08}"
template_mask_dec = "{:<8} {:<8} {:<8} {:<8}"

print(template_mask_1.format(mask_dec))
print(template_mask_dec.format(int(mask1_bin, 2), int(mask2_bin, 2), int(mask3_bin, 2), int(mask4_bin, 2)))
print(template_mask_bin.format(int(mask1_bin), int(mask2_bin), int(mask3_bin), int(mask4_bin)))

#print("\n", mask)
#print(mask1_bin, " ", mask2_bin)
