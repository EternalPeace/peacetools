# -*- coding: utf-8 -*-
'''
Author=yanyun
Email=yanyuneternal@163.com
'''
import httplib
def Scanweb(web):
    if web.__len__() == 0 :
        print "Website is required"
        return
    website = web
    #login path
    dirs = ["admin","login","admin_index","admin/admin","admin/login","admin/index","admin/user"]

    for line in dirs:
        conn = httplib.HTTPConnection(website)
        conn.request('GET','/'+line)
        r1 = conn.getresponse()
        if r1.status == 200 or r1.status == 301:
            print "********************************Great get something*************************************"
            print website+'/'+line,r1.status,r1.reason
        conn.close()
        conn = httplib.HTTPConnection(website)
        conn.request('GET','/'+line+'.asp')
        r1 = conn.getresponse()
        if r1.status == 200 or r1.status == 301:
            print "********************************Great get something*************************************"
            print website+'/'+line+'.asp',r1.status,r1.reason
        conn.close()
        conn = httplib.HTTPConnection(website)
        conn.request('GET','/'+line+'.php')
        r1 = conn.getresponse()
        if r1.status == 200 or r1.status == 301:
            print "********************************Great get something*************************************"
            print website+'/'+line+'.php',r1.status,r1.reason
        conn.close()
