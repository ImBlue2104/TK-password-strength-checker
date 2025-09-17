from tkinter import Button, Label, Entry, Toplevel, Tk

#Create Window
root = Tk()
root.title("Password Strength Checker App")
root.geometry("400x600")

welcome_msg = Label(text = "Welcome to the Password Strength Checker App", fg="white", bg="black").pack()
description_msg = Label(text="Enter your password to check its strength based on length!",fg="white", bg="black").pack()
password_input = Entry().pack()

