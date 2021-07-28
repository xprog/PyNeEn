# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'OSPF        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route_template = '''Protocol:              {protocol}
Prefix:                {prefix}
AD/Metric:             {ad_metric}
Next-Hop:              {next_hop}
Last update:           {last_update}
Outbound Interface     {interface}'''

ospf_route.strip().split()

protocol, prefix, ad_metric, via, next_hop, last_update, interface = ospf_route.strip().split()

print(ospf_route_template.format(protocol = protocol, prefix = prefix, ad_metric = ad_metric[1:-1], next_hop = next_hop.strip(","), last_update = last_update.strip(","), interface = interface))

