from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    print("pwd")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site_name = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(site_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="warning", message="site name or password can not be empty !")
    else:
        is_ok = messagebox.askokcancel(title="data confirm", message=f"Here are the information entered:\n "
                                                                     f"website={site_name}\n"
                                                                     f"password={password}\n Is it ok to save?\n")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{site_name} | {username} | {password}\n")
                # print(f"{site_name} | {username} | {password}")
            site_entry.delete(0, END)
            password_entry.delete(0, END)


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
site_entry.focus()  # let the cursor into this entry , so that user could start typing here straight away

username_entry = Entry(width=35)
# user insert to prefill the data in the entry, 0 means the start of the entry
username_entry.insert(0, "oren@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

pwd_button = Button(text="Generate Password", command=generate_password)
pwd_button.grid(row=4, column=1)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
