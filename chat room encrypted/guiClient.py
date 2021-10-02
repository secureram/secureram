import socket
import threading
from DFHME import DH_Endpoint
from PrimeNo import PrimeNo
import random

# from client import client
from encrypt import ENC
from tkinter import *


self = Tk()
self.title("CHAT ROOM {END-TO-END-ENCRYPTED}")
self.configure(bg='#000')
encrp = ENC()
client = socket.socket()
clientkeyone = []# list for key to store

#defining main function which is called when start button is clicked
def main():
    global  client
    self.update()
    global messagelist
    hostVar = hostEntry.get()# getting the value from entry
    port = int(portVar.get())#getting value from entry
    # Connecting To Server
    client.connect((hostVar, port))#connecting server

    # keys
    p = PrimeNo()#generating keys
    a = p.prime()
    pubkey = random.choice(a)
    a.pop(a.index(pubkey))# removing public key from the list to avoid repetation
    privkey = random.choice(a)


    # DFHMKE
    client.send(bytes(str(pubkey), 'utf-8'))
    pub2 = int(float(client.recv(1024).decode('utf-8')))
    clientkey = DH_Endpoint(pubkey, pub2, privkey)
    partialkey = clientkey.generate_partial_key()
    client.send(bytes(str(partialkey), 'utf-8'))
    partial2 = int(float(client.recv(1024).decode('utf-8')))
    key = clientkey.generate_full_key(int(partial2))
    clientkeyone.append(key)
    print(key)


    # defining functions

    def receive():#always ready to receive and decrypt
        while True:
            global  clientkeyone
            key = clientkeyone[0]
            message = client.recv(1024).decode('utf-8')
            dmessage = encrp.decrypt_message(message, key)
            messagelist.insert(END, dmessage)# this is our list which will be in our scroll bar

# starting thread for receiving
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()




def sendall():# sending message to server
    global client
    key = clientkeyone[0]
    name = setsEntry.get()
    sendt = sendVar.get()
    #inputuser =input(" ")
    message = name + ":"+ sendt
    client.send(bytes(encrp.encrypt_message(message, key), 'utf-8'))
    sendVar.set("")

def quit():# when clicked detaches from server safely and removes the previous key
    global clientkeyone
    client.detach()
    clientkeyone = []
def reset():# resets the entries and starts a new socket
    global client
    hostEntry.delete(0, END)
    portVar.set('12345')
    client = socket.socket()
    self.update()


#name label and entry
setsLabel = Label(self, text = "YOUR NAME" , bg='#000', fg='#fff',font=("Arial", 30))
setsLabel.pack()
setsEntry = Entry(self,  bg='#000', fg='#fff', justify='center',font=("Arial", 30), width= 50)
setsEntry.pack()



#host ip
hostLabel = Label(self, text = "HOST NAME :", bg='#000', fg='#fff',font=("Arial", 30))
hostLabel.pack()
hostEntry = Entry(self, bg='#000', fg='#fff', justify='center',font=("Arial", 30), width= 50)
hostEntry.pack()
#hostVar.set()
#host = hostVar.get()




#port num
portLabel = Label(self, text="PORT NUMBER:",bg='#000', fg='#fff', font=("Arial", 30))
portLabel.pack()
portVar = DoubleVar()
portEntry = Entry(self, textvariable=portVar, bg='#000', fg='#fff', justify='center',font=("Arial", 30), width= 50)
portEntry.pack()
portVar.set("1234")


##
#start chat
b = Button(self, text = "START CHAT", command =main, bg='#000', fg='#000', pady=20, padx=5 )
b.pack()

#this is our scroll bar where all the messages are reflected
receivearea = Scrollbar(self)
receivearea.pack(side = RIGHT , fill = Y, ipady = 40 ,ipadx = 10)
messagelist = Listbox(self, yscrollcommand = receivearea.set, bg='#699',font=("Arial", 30), width= 50)
messagelist.pack(side = BOTTOM , fill = BOTH, ipady = 40)
receivearea.config( command = messagelist.yview )

#send label
sendLabel = Label(self, text = "Let's Send Somthing! : " , bg='#000', fg='#fff',font=("Arial", 30))
sendLabel.pack()
sendVar = StringVar()
sendEntry = Entry(self,textvariable= sendVar,  bg ='#000' , fg='#fff',font=("Arial", 40), width= 100)
sendEntry.pack()

#button for reset
br = Button(self, text="RESET", command=reset, bg='#000', fg='#000', pady=20, padx=5, font=("Arial", 10))
br.pack(side=LEFT)
#button to quit
bq = Button(self, text="QUIT", command=quit, bg='#000', fg='#000', pady=20, padx=5, font=("Arial", 10))
bq.pack(side=RIGHT)
#button to send message
bs = Button(self, text = "SEND >>>", command =sendall, bg='#000', fg='#000', pady=20, padx=5,font=("Arial", 30)  )
bs.pack()

# GUI in loop so only exits when window is closed
self.mainloop()




