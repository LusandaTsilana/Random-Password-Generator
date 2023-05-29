from tkinter import *
from random import randint
from tkinter import messagebox

root = Tk()
root.configure(bg="white")
root.title('Code Breakers - Password Generator')
root.iconbitmap('images/password-icon-1.jpg')
root.geometry("500x300")


#generate random strong password
def new_rand():
    #to clear the entry box
    pw_entry.delete(0, END)
    
    #to get password length and convert to integer
    pw_length = int(my_entry.get())
    
    #create variabl to hold password
    password = ""
    
    #loop through password length
    for x in range(pw_length):
        password += chr(randint(33,126))
        
    #output password to the text box
    pw_entry.insert(0, password)
    

#copy to clipboard   
def clipper():
    #clear clipboard of anything that is already there
    root.clipboard_clear()
    #copy to clipboard
    root.clipboard_append(pw_entry.get())
    #pop up for successful copying
    messagebox.showinfo("Clipboard", "Copy Successful! Please go to Sign Up Page to continue")

#labelframe
labelframe = LabelFrame(root, text="How Many Characters?")
labelframe.pack(pady=20)

#create entry box to designate number of character
my_entry = Entry(labelframe, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#creating the entry box for the returned password
pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface" )
pw_entry.pack(pady=20)

#creating a frame for the buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#create the buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()