import socket                    
import random as r

def honeypot():

    s = socket.socket()
    
    vulnPorts = [20,21,22,23,25,53,137,139,445,80,443,8080,8443,1433,1434,3306,3389]

    choice = r.randint(0,len(vulnPorts))
    port = vulnPorts[choice]
    s.bind(('',port))

    print(f'\nHoney pot waiting for bee on honey port {port}.\n')

    s.listen()

    while 68 < 69:
        c, bee = s.accept()
        print(f'{bee} has tasted the honey port.')
        c.close()

honeypot()
