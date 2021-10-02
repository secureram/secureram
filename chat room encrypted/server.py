"""

"""

import socket
import threading
from DFHKE import  DH_Endpoint
from PrimeNo import PrimeNo
import random
from encrypt import ENC
from threading import *
import time

s = socket.socket()

s.bind(('localhost', 1234))

s.listen(100)
# keys
p = PrimeNo()#creating random prime no
a = p.prime()
pubkey = random.choice(a)# removing the no. from the list so that it wont repeat
a.pop(a.index(pubkey))
privkey = random.choice(a)

# list
keys = []
clients = []
encrp = ENC()




# defining functions

def sendall(message):
     for client in clients:# for every client and its perticular key is used to encrypt message and send
         index = clients.index(client)
         key = keys[index]
         client.send(bytes(encrp.encrypt_message(message, key),'utf-8'))




def receive(client):
    while True:# always listens and if receives sends all
        message = client.recv(1024).decode()
        index = clients.index(client)
        key = keys[index]
        dmessage = encrp.decrypt_message(message, key)
        sendall(dmessage)




def handle():
    while True:
      #diffi hellman exchange is started
        client, address = s.accept()
        client.send(bytes(str(pubkey), 'utf-8'))
        pub2 = int(float(client.recv(1024).decode()))
        serverkey = DH_Endpoint(pub2, pubkey, privkey)
        partialkey = serverkey.generate_partial_key()
        client.send(bytes(str(partialkey), 'utf-8'))
        partial2 = int(float(client.recv(1024).decode()))
        key = serverkey.generate_full_key(partial2)
        print("Connected with {}".format(str(address)))
        keys.append(key)
        clients.append(client)
        # key is generated and appended to the key list 
        # thread is started for a particular client to receive message
        thread = threading.Thread(target=receive, args=(client,))
        thread.start()
        



handle()
