from tkinter import *
from random import randint
from tkinter import messagebox  # Import messagebox module

root = Tk()
root.title('Strong Password Generator')
root.geometry("500x300")


# Generate Random Password
def new_rand():
    # Clear the Entry Box
    pw_entry.delete(0, END)
    # Get password length and convert to an integer
    pw_length = int(my_entry.get())

    # Create a variable to hold the password
    my_password = ''

    # Loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # Output password to the screen
    pw_entry.insert(0, my_password)


# Copy to Clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Password Copied", "Password copied to clipboard!")


lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=copy_to_clipboard)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
