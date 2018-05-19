# Name: Rohan Pote
# Final project
# Pyhton 2

import Tkinter as tk
from customer import *
from admin import *
import sqlite3
import tkMessageBox

#------------- To verify username, password and to display the options as per the user
def menu(username, password):
	with sqlite3.connect("finalproject.db") as conn:
		search = conn.execute("select * from userdata where uname=? and pwd=?", (username, password,))
		row = search.fetchone()
		global userid
		userid = row[2]
		global num
		num = row[0]
		if row == None:
			tkMessageBox.showinfo("Oops!", "This user does not exists")
		elif (username.lower() == 'admin' and password.lower() == 'admin'):
			myapp = tk.Tk()
			myapp.geometry("1366x768")
			admin_label = tk.Label(myapp, text = "Welcome Administrator", font="Calibri 16 bold italic")
			admin_label.place(x=180, y=10)
			myapp.title("Administrator")
			admin_display_button = tk.Button(myapp, text="Display Inventory", width=30, command=display_inventory)
			admin_display_button.pack()
			admin_add_button = tk.Button(myapp, text="Add / Update Items", width=30, command=add_items)
			admin_add_button.pack()
			admin_remove_button = tk.Button(myapp, text="Remove Items", width=30, command=remove_items)
			admin_remove_button.pack()
			admin_display_button.place(x=200, y=100)
			admin_add_button.place(x=200, y=150)
			admin_remove_button.place(x=200, y=200)
			
		else: 	
			myapp = tk.Tk()
			myapp.geometry("1366x768")
			myapp.title("The Laptop Store")
			customer_label = tk.Label(myapp, text = "Welcome to The Laptop Store", font="Calibri 16 bold italic")
			customer_label.place(x=100, y=50)
			option_label = tk.Label(myapp, text="Please select from the below options: ")
			option_button1 = tk.Button(myapp, text="1. Create a new order", width=30, command=lambda: create_order(userid))
			option_button2 = tk.Button(myapp, text="2. View Cart details", width=30, command=lambda: view_cart(userid))
			option_button3 = tk.Button(myapp, text="3. Modify an existing order", width=30, command=modify_order)
			option_button4 = tk.Button(myapp, text="4. Delete an order", width=30, command=delete_order)
			option_label.place(x= 100, y=100)
			option_button1.place(x=100, y=200)
			option_button2.place(x=100, y=250)
			option_button3.place(x=100, y=300)
			option_button4.place(x=100, y=350)
	