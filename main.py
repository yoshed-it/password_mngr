
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    get_website = website_entry.get()
    get_email = email_usrname_entry.get()
    get_password = password_entry.get()
    
    
    if len(get_email) == 0 or len(get_password) == 0:
        messagebox.showerror('Error', 'Please No Empty Fields')
    else: 
        is_ok = messagebox.askokcancel(title=get_website, message=f"Email: {get_email}\n Password: {get_password}\n Is This Correct?")
        if is_ok :
            with open("/Users/aestheticsseattle/Desktop/Yosh_Jazz/Programmin/Python/password_mngr/password.txt", "a") as pass_file:
                pass_file.write(f"{get_website} | {get_email} | {get_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PassMan")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="/Users/aestheticsseattle/Desktop/Yosh_Jazz/Programmin/Python/password_mngr/logo.png")

canvas.create_image(100, 100, image=logo)

website_txt = Label(text="Website:")
email_usrname = Label(text="Email/Username:")
password = Label(text="Password:")


website_entry = Entry(width=37)
website_entry.focus()

email_usrname_entry = Entry(width=37)
email_usrname_entry.insert(END, "yoshed-it@email.com")

password_entry = Entry(width=21)

add_btn = Button(width=35, text="Add", command=save_to_file)
gen_btn = Button(width=11, text="Generate Password")


# Grid Layout   
canvas.grid(column=1, row=1)
website_txt.grid(column=0, row=2)
email_usrname.grid(column=0, row=3)
password.grid(column=0, row=4)

website_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_usrname_entry.grid(column=1, row=3, columnspan=2, sticky=W)
password_entry.grid(column=1, row=4, sticky=W)

gen_btn.grid(column=2, row=4, sticky=W)
add_btn.grid(column=1, row=5, columnspan=3, sticky=W)


# ______________Remains at bottom

window.mainloop()