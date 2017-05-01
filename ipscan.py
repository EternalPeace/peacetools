# -*- coding: utf-8 -*-
‘’’
Author=yanyun
Email=yanyuneternal@163.com
‘’’
import platform
import os
import threading
import time
'''
call for example 
print "start time %s"%time.ctime()
ipscan.ipscan('192.168.1',2,255)
print "start time %s"%time.ctime()
'''
def get_os():
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"    
def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()
    #print cmd
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >=0:
            print "ip: %s is alive"%ip_str
            return
    #print "ip: %s is dead"%ip_str
def ipscan(ip_prefix,ip_b,ip_e):
    threads=[]
    for i in range(ip_b,ip_e):
        ip = '%s.%s'%(ip_prefix,i)
        #print ip
        
        t=threading.Thread(target=ping_ip,args=(ip,))
        threads.append(t)
    for t in threads:
        t.setDaemon(True)   
        t.start()
        time.sleep(0.1)
    t.join()
