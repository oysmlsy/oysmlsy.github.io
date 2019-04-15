#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'oysmlsy'

import datetime
import os
import re
import shutil
import sys


def _static_ip(interface, ipaddr, netmask, gateway, dns1='180.76.76.76', dns2='8.8.8.8', bootproto='static', onboot='yes', nm_controlled='no'):
    re_str = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if not re.match(re_str, ipaddr) or not re.match(re_str, netmask) or not re.match(re_str, gateway) or not re.match(re_str, dns1) or not re.match(re_str, dns2):
        raise TypeError('IP format error!')

    ifcfg_file = '/etc/sysconfig/network-scripts/ifcfg-%s' % interface
    if not os.path.exists(ifcfg_file):
        raise TypeError('%s does not exists!' % ifcfg_file)

    with open(ifcfg_file, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if 'BOOTPROTO' in line or 'ONBOOT' in line or 'NM_CONTROLLED' in line or 'IPADDR' in line or 'NETMASK' in line or 'PREFIX' in line or 'GATEWAY' in line or 'DNS' in line:
            pass
        else:
            new_lines.append(line)

    new_lines.append('\n')
    new_lines.append('IPADDR=%s\n' % ipaddr)
    new_lines.append('NETMASK=%s\n' % netmask)
    new_lines.append('GATEWAY=%s\n' % gateway)
    new_lines.append('DNS1=%s\n' % dns1)
    new_lines.append('DNS2=%s\n' % dns2)
    new_lines.append('BOOTPROTO=%s\n' % bootproto)
    new_lines.append('ONBOOT=%s\n' % onboot)
    new_lines.append('NM_CONTROLLED=%s\n' % nm_controlled)

    ifcfg_file_backup = '/etc/sysconfig/network-scripts/ifcfg-%s.backup.%s' % (interface, datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
    shutil.copy(ifcfg_file, ifcfg_file_backup)

    with open(ifcfg_file, 'w') as f:
        f.write(''.join(new_lines))


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 6:
        try:
            _static_ip(args[1], args[2], args[3], args[4], args[5])
            print('# Network config altered!')
            print('# Restarting network ...')
            if os.system('/usr/bin/systemctl restart network') == 0:
                print('# Succeed! Network restarted!')
            else:
                print('# Failed! Network failed to restart!')
        except TypeError, e:
            print('# Error! %s' % e.message)
        except Exception, e:
            print('# Error! %s' % e.message)

    else:
        print('')
        print('Usage: static_ip.py <interface> <ipaddr> <netmask> <gateway> <dns1>')
        print('')
