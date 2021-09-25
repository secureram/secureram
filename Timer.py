from tkinter import *
import time
import playsound


self = Tk()
# setting the title for our window
self.title("Excercise Timer")

#configuring background colour for our window
self.configure(bg="black")

#creating a variable basically this is our timer label
stime = StringVar()

#setting the initial value of the variable
stime.set("00")

#function
def func():

    nsets = int(setsVar.get()) #getting values from the sets entry
    wt = int(wtimeVar.get())# getting valuers from workout time entry
    rt = int(rtimeVar.get())# getting values from the relax time entry

    for count in range(nsets):

        playsound.playsound("start.mp3")  # using play sound module to play the sound from selected file

        for count in range(1, wt + 1):  # this is a loop of range workout time

            t = (wt - count)  # initializing a  local variable for the value of the second
            stime.set(t)  # setting the value 't' to our timer label
            self.update()  # updatind tkinter(GUI window) so that the value changes and updates in every loop 
            time.sleep(1) # this will wait for 1 sec and continues the loop 

        playsound.playsound("relax.mp3")# using play sound module to play the sound from selected file
        for count in range(1, rt + 1):# this is a loop of range relax time

            r = (rt - count) # initializing a  local variable for the value of the second
            stime.set(r) # setting the value 'r' to our timer label
            self.update() # updatind tkinter(GUI window) so that the value changes and updates in every loop 
            time.sleep(1) # this will wait for 1 sec and continues the loop

    playsound.playsound("congrats.mp3")# using play sound module to play the sound from selected file




# Now here we are setting our GUI window structure
#no.of exercises
setsLabel = Label(self, text = "NO.OF Exercises" , bg='#000', fg='#fff')  # This will create a label named NO.OF Excersices
setsLabel.pack()
setsVar = DoubleVar() # creating a variable
setsEntry = Entry(self, textvariable = setsVar, bg='#000', fg='#fff', justify='center') # creating a entry for the label above and assingnig the variable to store the input
setsEntry.pack()

#Wouts
wtimeLabel = Label(self, text = "Workout Time(seconds)", bg='#000', fg='#fff')# This will create a label named Workout Time(seconds)
wtimeLabel.pack()
wtimeVar = DoubleVar() # creating a variable 
wtimeEntry = Entry(self, textvariable = wtimeVar, bg='#000', fg='#fff', justify='center')# creating a entry for the label above and assingnig the variable to store the input
wtimeEntry.pack()
wtimeVar.set(45)# setting the deafault value of variable ; note since entry is assigned with this variable this reflects on the window

#relax time
rtimeLabel = Label(self, text="Relax time(seconds)",bg='#000', fg='#fff', )# This will create a label named Relax Time(seconds)
rtimeLabel.pack()
rtimeVar = DoubleVar()
rtimeEntry = Entry(self, textvariable=rtimeVar, bg='#000', fg='#fff', justify='center')# creating a entry for the label above and assingnig the variable to store the input
rtimeEntry.pack()
rtimeVar.set(20)# setting the deafault value of variable ; note since entry is assigned with this variable this reflects on the window


#button
b = Button(self, text = "START", command =func, bg='#000', fg='#000', pady=20, padx=5 )# setting up a button and assigning a function to perform when clicked.
b.pack()


# Timer Label
# note we have assigned the variable in the start of the script 

stimeLabel = Label(self, textvariable=stime, font=("Arial", 90), bg='#000', fg='#fff')# this is the label for our timer
stimeLabel.pack(padx=90, pady = 40)# setting the height, width, padding in x and y directions of the label.




self.mainloop()# calling the program in  a loop, functions untill the window is closed.
