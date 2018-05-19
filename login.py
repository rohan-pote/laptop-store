# Name: Rohan Pote
# Final project
# Pyhton 2

import Tkinter as tk
from signup import signup
from options import menu

myapp=tk.Tk()
myapp.geometry("1366x768")

#----- Login page GUI -----

def log():
	
	title_label = tk.Label(myapp, text = "Welcome to The Laptop Store")
	title_label.configure(font=("Calibri", 20))
	title_label.place(x=250, y=10)
	myapp.title("Laptop Store Login")

	login_label = tk.Label(myapp, text = "Login :")
	login_label.configure(font=("Calibri", 15))
	login_label.place(x=200, y=150)
	login_username_label = tk.Label(myapp, text = "Username: ")
	login_username_label.configure(font=("Calibri", 12))
	login_password_label = tk.Label(myapp, text = "Password: ")
	login_password_label.configure(font=("Calibri", 12))
	login_login_button = tk.Button(myapp, text="Login", command=lambda: menu(login_username_input.get(), login_password_input.get()))
	login_login_button.pack()
	login_signup_label = tk.Label(myapp, text="New Customer? Sign up here: ")
	login_signup_label.configure(font=("Calibri", 12))
	login_signup_button = tk.Button(myapp, text="Sign Up", command=signup)
	login_signup_button.pack()
	login_username_input = tk.Entry(myapp)
	login_password_input = tk.Entry(myapp, show="*")
	login_username_label.place(x=200, y=200)
	login_password_label.place(x=200, y=240)
	login_login_button.place(x=250, y=280)
	login_username_input.place(x=300, y=200)
	login_password_input.place(x=300, y=240)
	login_signup_label.place(x=200, y=350)
	login_signup_button.place(x=420, y=350)
	


log()
myapp.mainloop()
