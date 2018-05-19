# Name: Rohan Pote
# Final project
# Pyhton 2

import Tkinter as tk
import sqlite3
import tkMessageBox


#------------ Function for new user account creation 
def signup():
	myapp = tk.Tk()
	myapp.geometry("1366x768")
	myapp.title("Sign up")
	
	first_name_label = tk.Label(myapp, text="First Name: ")
	first_name_label.configure(font=("Calibri", 12))
	last_name_label = tk.Label(myapp, text="Last Name: ")
	last_name_label.configure(font=("Calibri", 12))
	username_label = tk.Label(myapp, text="Username: ")
	username_label.configure(font=("Calibri", 12))
	password_label = tk.Label(myapp, text="Password: ")
	password_label.configure(font=("Calibri", 12))
	first_name_input = tk.Entry(myapp)
	last_name_input = tk.Entry(myapp)
	username_input = tk.Entry(myapp)
	password_input = tk.Entry(myapp)
	create_account_button = tk.Button(myapp, text="Create Account", command=lambda: add_data(first_name_input.get(), last_name_input.get(), username_input.get(), password_input.get()))
	create_account_button.pack()
	back_button = tk.Button(myapp, text="exit")
	back_button.pack()
	
		
	first_name_label.place(x=100, y= 100)
	first_name_input.place(x=250, y=100)
	last_name_label.place(x=100, y=130)
	last_name_input.place(x=250, y=130)
	username_label.place(x=100, y=160)
	username_input.place(x=250, y=160)
	password_label.place(x=100, y=190)
	password_input.place(x=250, y= 190)
	create_account_button.place(x=150, y=230)
	back_button.place(x=300, y=230)

def add_data(first_name, last_name, username, password):
	with sqlite3.connect("finalproject.db") as conn:
		search = conn.execute("select * from userdata where uname=?", (username,))
		row = search.fetchone()
		if row == None:
			conn.execute("insert into userdata values (?,?,?,?)", (first_name, last_name, username, password))
			tkMessageBox.showinfo("Success!", "Account created Successfully!!")
		else:
			tkMessageBox.showerror("Error!", "This username already exists!")
	
	
	
	
	
	
	
