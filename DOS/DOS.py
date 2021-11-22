import socket
import time
import threading

requests = """GET / HTTP/1.1
Host: HOSTNAME
"""

def slowl():
    s = socket.socket()
    s.connect(("HOSTNAME", 80))
    s.send(requests.encode())
    print(s.recv(1024))
    s.close()


for i in range(100000):
    send_thread = threading.Thread(target=slowl)
    send_thread.start()
    time.sleep(0.5)
