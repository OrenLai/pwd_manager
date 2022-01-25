from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    print("pwd")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    print("add to file")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

site_entry = Entry(width=35)
site_entry.grid(row=1, column=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

pwd_button = Button(text="Generate Password", command=generate_password)
pwd_button.grid(row=4, column=1)

add_button = Button(text="Add", width=32, command=add_to_file)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
