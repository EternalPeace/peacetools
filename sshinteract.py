# -*- coding: utf-8 -*-
'''
from Internet
'''
# -*- coding: utf-8 -*-
'''
usage
    import sshinteract
    host = '192.168.1.12'
    user = 'root'
    password = 'root'
    shellcmd = sshinteract.sshconnect(user, host, password)
    sshinteract.send_command(shellcmd, 'cat /etc/shadow | grep root')
'''
import pexpect

PROMPT = ['# ', '>>> ', '> ','\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def sshconnect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,\
                        '[P|p]assword:'])
    
    if ret == 0:
        print '[-] Error Connecting'
        return
    
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, \
                            '[P|p]assword:'])
        if ret == 0:
            print '[-] Error Connecting'
            return    
    child.sendline(password)
    child.expect(PROMPT)
    return child

