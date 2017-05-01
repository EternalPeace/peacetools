# -*- coding: utf-8 -*-
‘’’
Author=yanyun
Email=yanyuneternal@163.com
‘’’
import nmap # import nmap.py module
import optparse  
def scanonce(tgtHost, tgtPort):  
    #nmapscan('127.0.0.1','22,80')
    nmScan = nmap.PortScanner()  
    nmScan.scan(tgtHost, tgtPort)  
    #get the port state  
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']  
    print " [*] " + tgtHost + " tcp/" + tgtPort + " " + state  
def nmapscan(tgtHost,tgtPort):  
    tgtHost = tgtHost  
    tgtPorts = str(tgtPort).split(",")  
    if (tgtHost == None) | (tgtPorts[0] == None):  
        print "Should define tgtHost and tgtPorts"  
        exit(0)  
    for tgtPort in tgtPorts:  
        scanonce(tgtHost, tgtPort)  
def nmaprangescan(tgtHost,PortB,PortE):  
    #for example nmaprangescan('127.0.0.1',26,29),port 29 will not be scanned
    tgtHost = tgtHost  
    if PortB > PortE:
        print "PortBegin should smaller than PortEnd"
        return 
    for tgtPort in range (PortB,PortE):  
        scanonce(tgtHost, str(tgtPort)) 