#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re
import time

vuln_ports = ['3311', '3312', '3389', '4440', '5672', '5900', '6082', '6379',\
                            '7001', '8080', '8089', '8161', '8649', '9000', '9090', '9200', '9300', '9999', \
                            '10050', '11211', '27017', '28017', '3777', '50000', '50060', '50070', '21', \
                            '22', '23', '25', '53', '123', '161', '162', '8161', '8161', '389', '512', \
                            '513', '873', '1433', '1080', '1521', '1900', '2049', '2601', '2604', '2082', \
                            '2083', '3128', '3312', '3306', '4899', '4440', '8834', '4848']


def get_vulu_port_infos():
    vulu_port_infos = []
    foo_str = ''
    biaoji = 0
    with open('port_baidu_submain_nmap.txt', 'r') as f:
        for line in f:
            if 'Nmap' in line:
                biaoji += 1
                if biaoji == 2:
                    vulu_port_infos.append(foo_str)
                    foo_str = ''
                    foo_str += line
                    biaoji = 1
            else:
                foo_str += line
    return vulu_port_infos


def check_eque_list(a, b):
    for i in a:
        for j in b:
            if i == j:
                return 1


def write_to_file(arg1):
    with open('vuln_port_baidu_submain_nmap.txt', 'w') as f:
        f.writelines(arg1)


if __name__ == '__main__':
    acque_vuln_ports_ip = []
    port_re = re.compile(r'([0-9]{1,6})')
    vuln_port_infos = get_vulu_port_infos()
    for vulu_port_info in vuln_port_infos:
        try:

            vulu_port_info_not_ip = vulu_port_info.split('Host')[1]

            ports = [port for port in port_re.findall(vulu_port_info_not_ip)]
            if check_eque_list(ports, vuln_ports) == 1:
                acque_vuln_ports_ip.append(vulu_port_info)
        except IndexError:
            pass
    write_to_file(acque_vuln_ports_ip)
