import socket
import random

def testport(ip,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((ip,port))
        print 'Server port '+ str(port)+ ' OK!'
    except Exception:
        print 'Server port '+ str(port)+ ' not connect!'
        sk.close()
    return 

def randomip():
    o1=random.randint(0,254)
    o2=random.randint(0,255)
    o3=random.randint(0,255)
    o4=random.randint(1,254)
    while (o1 == 127 or o1 == 0 or o1 == 56 or o1 == 10 or o1 == 3 or o1 == 6 or o1 == 7 or o1 == 11 or o1 == 21 or o1 == 22 or o1 == 26 or o1 == 28 or o1 == 29 or o1 == 30 or o1 == 33 or o1 == 55 or o1 == 214 or o1 == 215 or o1 == 15 or o1 == 16 or ( o1 == 192 and o2 == 168 ) or ( o1 == 172 and o2 >= 16 and o2 <32) or ( o1 == 100 and o2 >= 64 and o2 < 127) or ( o1 == 169 and o2 > 254 ) or ( o1 == 198 and o2 >= 18 and o2 < 20)):
        o1=random.randint(0,254)
        o2=random.randint(0,255)
        o3=random.randint(0,255)
        o4=random.randint(1,254)
    randomip=str(o1)+'.'+str(o2)+'.'+str(o3)+'.'+str(o4)
    return randomip

ip=randomip()
print ip





#    while (o1 == 127 ||                             // 127.0.0.0/8      - Loopback
#          (o1 == 0) ||                              // 0.0.0.0/8        - Invalid address space
#          (o1 == 3) ||                              // 3.0.0.0/8        - General Electric Company
#          (o1 == 15 || o1 == 16) ||                 // 15.0.0.0/7       - Hewlett-Packard Company
#          (o1 == 56) ||                             // 56.0.0.0/8       - US Postal Service
#          (o1 == 10) ||                             // 10.0.0.0/8       - Internal network
#          (o1 == 192 && o2 == 168) ||               // 192.168.0.0/16   - Internal network
#          (o1 == 172 && o2 >= 16 && o2 < 32) ||     // 172.16.0.0/14    - Internal network
#          (o1 == 100 && o2 >= 64 && o2 < 127) ||    // 100.64.0.0/10    - IANA NAT reserved
#          (o1 == 169 && o2 > 254) ||                // 169.254.0.0/16   - IANA NAT reserved
#          (o1 == 198 && o2 >= 18 && o2 < 20) ||     // 198.18.0.0/15    - IANA Special use
#          (o1 >= 224) ||                            // 224.*.*.*+       - Multicast
#          (o1 == 6 || o1 == 7 || o1 == 11 || o1 == 21 || o1 == 22 || o1 == 26 || o1 == 28 || o1 == 29 || o1 == 30 || o1 == 33 || o1 == 55 || o1 == 214 || o1 == 215) // Department of Defense 
