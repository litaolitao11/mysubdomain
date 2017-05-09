#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
     get ip for txt from subDomainsBrute.py
"""

import re


def getIP_list():
    ipaddr = []
    with open('baidu.com.txt', 'r') as f:
        for line in f:
            reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
            for ip in reip.findall(line):
                ipaddr.append(ip)
    return ipaddr


if __name__ == '__main__':
    ipaddrs = getIP_list()
    with open('ipaddr_baidu.txt', 'w') as f:
        for ipaddr in ipaddrs:
            f.write(ipaddr+'\n')
