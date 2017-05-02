# -*- coding: utf-8 -*-
'''
Author=yanyun
Email=yanyuneternal@163.com
'''
#passwords.txt store the password need to be cracked
#dictionary.txt  sotre the dictionary
import crypt
def SHAPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print 'Great!Found The Password: ' + word + '\n'
            return
    print 'Sorry Password Not Found.\n'
    return
def SHA512Pass(cryptPass):
    print 'SHA512 crack have not completed.\n'
    return
def passcrack(mtype):
    #passwords.txt from /etc/shadow,u can select the lines u need to crack.
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print user + '\'s password is being cracked ' 
            if mtype == 'SHA':
                SHAPass(cryptPass)
            elif mtype == 'SHA512':
                SHA512Pass(cryptPass)
            else:
                print "Using passcrack('SHA512') or passcrack('SHA') please!"

