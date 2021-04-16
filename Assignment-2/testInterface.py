from tkinter import *
from Interface import phraseinput as pi

opcode = 0

root = Tk() 
root.geometry("550x700") 
root.resizable(width=False, height=False)
root.title(" Robot Robert ")

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    if (INPUT == ""): Output.insert(END, "PLEASE INPUT A SENTENCE.\n")
    else:
        global opcode
        Output.insert(END, ("User: " + INPUT + "\n"))
        response = pi.interpolate(opcode, INPUT)
        opcode = response[0:1]
        OUTPUT = response[1:] 
        Output.insert(END, OUTPUT)

l = Label(text = "Robot Robert", font='Helvetica 18 bold')

Output = Text(root, height = 18,  
              width = 65,  
              bg = "white") 

inputtxt = Text(root, height = 2, 
                width = 65, 
                bg = "white") 
 
Display = Button(root, height = 2, 
                 width = 10,  
                 text ="Send", 
                 command = lambda:Take_input()) 

l.pack(expand=TRUE)  
Output.pack(expand=TRUE) 
inputtxt.pack(expand=TRUE)
Display.pack(expand=TRUE) 
  
mainloop() 