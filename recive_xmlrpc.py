#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xmlrpc.client
import subprocess
import time

XMLRPC_HOST = '192.168.8.167'
XMLRPC_PORT = 8000

client = xmlrpc.client.ServerProxy('http://%s:%d' % (XMLRPC_HOST, XMLRPC_PORT))

cmd = 'hostname -I | cut -d\' \' -f1'
IP = subprocess.check_output(cmd, shell = True) #получаем IP
IP = IP.rstrip().decode("utf-8") #удаляем \n, переводим в текст

while(True):
    print('OK')
    print(client.play(IP))
    time.sleep(10)
    print(client.stop())
    time.sleep(10)
