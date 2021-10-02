import socket
import threading
from DFHME import DH_Endpoint
from PrimeNo import PrimeNo
import random
from encrypt import ENC

# Choosing Nickname
# nickname = input("Choose your nickname: ")
name = input("please enter your name: ")
# Connecting To Server
client = socket.socket()
client.connect(('localhost', 1234))

# keys
p = PrimeNo()
a = p.prime()
pubkey = random.choice(a)
a.pop(a.index(pubkey))
privkey = random.choice(a)
encrp = ENC()

# DFHMKE
client.send(bytes(str(pubkey), 'utf-8'))
pub2 = int(float(client.recv(1024).decode('utf-8')))
clientkey = DH_Endpoint(pubkey, pub2, privkey)
partialkey = clientkey.generate_partial_key()
client.send(bytes(str(partialkey), 'utf-8'))
partial2 = int(float(client.recv(1024).decode('utf-8')))
key = clientkey.generate_full_key(int(partial2))
print(key)


# defining functions

def receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        print(encrp.decrypt_message(message, key))

def main():
    while True:
        inputuser =input(" ")
        message = name + ":"+ inputuser
        client.send(bytes(encrp.encrypt_message(message, key), 'utf-8'))

# defining threads and starting them

receive_thread = threading.Thread(target=receive)
receive_thread.start()
main_thread = threading.Thread(target=main)
main_thread.start()
