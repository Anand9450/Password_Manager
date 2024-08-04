from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '~', '<', '>', '?']

    n_letters = random.randint(8,10)
    n_symbols = random.randint(2,4)
    n_numbers = random.randint(2,4)

    password_list = []
    for char in range(1, n_letters+1):
        password_list.append(random.choice(letters))
    for char in range(1, n_symbols+1):
        password_list.append(random.choice(symbols))
    for char in range(1, n_numbers+1):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password = ''
    for char in password_list:
        password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email is: {email}\n"
                                                       f"Password is: {password}\n")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any field empty")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the entered: \nEmail: {email}"
        #                                               f"\nPassword: {password}\nIs it ok to save")
        # if is_ok:
        try:
            with open("data.json","r") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                #reading old json data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            #saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(height=250, width=200)
logo_img = PhotoImage(file="img.png")
canvas.create_image(100,100, image= logo_img)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)
email_label = Label(text="Username/Email: ")
email_label.grid(row=2,column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=32)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0,"aananddshukla@gamil.com")
password_entry = Entry(width=32)
password_entry.grid(row=3,column=1)

#Buttons
search_button = Button(text="Search", width=14, command=find_password )
search_button.grid(row= 1, column= 2)
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="ADD",width=42, command=save)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()