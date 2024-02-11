import socket                    
import random as r

def honeypot():

    hive = socket.socket()
    
    honey = [20,21,22,23,25,53,137,139,445,80,443,8080,8443,1433,1434,3306,3389]

    choice = r.randint(0,len(honey))
    honeyDrop = honey[choice]
    hive.bind(('',honeyDrop))

    print(f'\nHoney pot waiting for bee on honey port {honeyDrop}.\n')

    hive.listen()

    while 68 < 69:
        queen, foreignBee = hive.accept()
        print(f'{foreignBee} tried to take honey from honey port {honeyDrop}.')
        queen.close()
        print(f'Queen Has kicked foreign bee out.\n')

honeypot()
              
