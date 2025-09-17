from tkinter import Button, Label, Entry, Toplevel, Tk

#Create Window
root = Tk()
root.title("Password Strength Checker App")
root.geometry("400x600")

welcome_msg = Label(root,text = "Welcome to the Password Strength Checker App", fg="white", bg="black").pack()
description_msg = Label(root,text="Enter your password to check its strength based on length!",fg="white", bg="black").pack()
password_input = Entry(root).pack()

#function t check password strength
def strength_check():
    password_len = password_input.get()
    password_strength = 'placeholder'

    #if-else conditionl to check strength based length.
    if password_len > 12:
        password_strength = 'Very Strong'
    elif password_len > 8:
        password_strength = 'Strong'
    elif 6 <= password_len <= 8:
        password_strength = 'Medium'
    else:
        password_strength = ' Weak'

    #if-else to assign color and display on root
    if password_strength == 'Very Strong':
        Label(root, text = "Your password Strength is Very Strong!", fg = 'white', bg = 'Dark Green')
    elif password_strength == 'Strong':
        Label(root, text = "Your password Strength is Strong!", fg = 'black', bg = 'Green')
    elif password_strength == 'Strong':
        Label(root, text = "Your password Strength is Medium", fg = 'black', bg = 'Yellow')
    else:
        Label(root, text = "Your password Strength is Weak :(", fg = 'white', bg = 'Red')

        