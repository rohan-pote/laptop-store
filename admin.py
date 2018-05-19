# Name: Rohan Pote
# Final project
# Pyhton 2


import Tkinter as tk 
import sqlite3
import tkMessageBox


def display_inventory():

	myapp = tk.Tk()
	myapp.title("Inventory")
	myapp.geometry("640x480")
	
	with sqlite3.connect("finalproject.db") as conn:
		result = conn.execute("Select * from inventory;")
		row = result.fetchall()
		for i in range(len(rows)):
			laptop_label = tk.Label(myapp, text = rows[i][0])
			laptop_label.place(row=i, column=1)
			spec_label = tk.Label(myapp, text = rows[i][1])
			spec_label.place(row=i, column=2)
			price_label = tk.Label(myapp, text = rows[i][2])
			price_label.place(row=i, column=3)
			qty_label = tk.Label(myapp, text = rows[i][3])
			qty_label.place(row=i, column=4)

			
#----------- GUI to add products to the inventory----------------			
def add_items():
	myapp = tk.Tk()
	myapp.title("Manage Inventory")
	myapp.geometry("1366x768")
	
	item_id_label = tk.Label(myapp, text="Product ID: ")
	item_id_entry = tk.Entry(myapp)
	laptop_name_label = tk.Label(myapp, text="Laptop Name: ")
	laptop_name_entry = tk.Entry(myapp)
	specification_label = tk.Label(myapp, text="Specifications: ")
	specification_text = tk.Text(myapp, width=50, height=10)
	price_label = tk.Label(myapp, text="Price: ")
	price_entry = tk.Entry(myapp)
	quantity_label = tk.Label(myapp, text="Quantity: ")
	quantity_entry = tk.Entry(myapp)
	
	item_id_label.place(x=100, y=50)
	item_id_entry.place(x=300, y=50)	
	laptop_name_label.place(x=100, y=100)
	laptop_name_entry.place(x=300, y=100)
	specification_label.place(x=100, y=150)
	specification_text.place(x=300, y=150)
	price_label.place(x=100, y=350)
	price_entry.place(x=300, y=350)
	quantity_label.place(x=100, y=400)
	quantity_entry.place(x=300, y=400)
	
	add_button = tk.Button(myapp, text="Add", command=lambda: add_to_inventory(item_id_entry.get(), laptop_name_entry.get(), specification_text.get(1.0, 10.50), price_entry.get(),quantity_entry.get()))
	add_button.place(x=100, y=450)

#---------Function to add/update products in database-----------------
def add_to_inventory(item_id,laptop_name,specifications,price,quantity):
	with sqlite3.connect("finalproject.db") as conn:
		search = conn.execute("select * from inventory where item_id=?", (item_id,))
		row = search.fetchone()
		if row == None:
			conn.execute("insert into inventory values (?,?,?,?,?)", (item_id,laptop_name,specifications,price,quantity))
			tkMessageBox.showinfo("Successful!", "Item Added Successfully!!")
		else:
			conn.execute("update inventory set laptop_name=?, specifications=?, price=?, quantity=? where item_id=?", (laptop_name,specifications,price,quantity, item_id))
			tkMessageBox.showinfo("Successful!", "Item Updated Successfully!!")
	
	
	
#----------- GUI for removing items --------------			
def remove_items():
	myapp = tk.Tk()
	myapp.title("Manage Inventory")
	myapp.geometry("1366x768")
	
	itemid_label = tk.Label(myapp, text="Item ID: ")
	itemid_entry = tk.Entry(myapp)
	remove_button = tk.Button(myapp, text="Remove Product from Inventory", command=lambda: remove_from_inventory(itemid_entry.get()))
	
	itemid_label.place(x=100, y=50)
	itemid_entry.place(x=300, y=50)	
	remove_button.place(x=100, y=150)

	
#----------- function to remove items from database -------------------	
def remove_from_inventory(itemid):
	with sqlite3.connect("finalproject.db") as conn:
		search = conn.execute("select * from inventory where item_id=?", (itemid,))
		row = search.fetchone()
		if row == None:
			tkMessageBox.showinfo("Incorrect!", "This product does not exist")
		else:
			conn.execute("delete from inventory where item_id=?", (itemid,))
			tkMessageBox.showinfo("Success!", "Product removed successfully")
			

# --------------- To Display products in inventory --------------------
def display_inventory():
	myapp=tk.Tk()
	myapp.title("Inventory")
	myapp.geometry("1366x768")
	
	inventoryframe = tk.Frame(myapp)
	inventoryframe.pack()
	
	
	with sqlite3.connect("finalproject.db") as conn:
		result = conn.execute("select * from inventory")
		rows = result.fetchall()
		item_label = tk.Label(inventoryframe, text="Product ID", bg="light blue", width = 10, borderwidth=1, relief="solid")
		lp_label = tk.Label(inventoryframe, text = "Laptop Name", bg="light blue", width = 20, borderwidth=1, relief="solid")
		sp_label = tk.Label(inventoryframe, text="Specifications", bg="light blue", width=21, borderwidth=1, relief="solid")
		pr_label = tk.Label(inventoryframe, text="Price ($)", bg="light blue", width=10, borderwidth=1, relief="solid")
		qt_label = tk.Label(inventoryframe, text="Quantity", bg="light blue", width=10, borderwidth=1, relief="solid")
		item_label.grid(row=0, column=1)
		lp_label.grid(row=0, column=2)
		sp_label.grid(row=0, column=3)
		pr_label.grid(row=0, column=4)
		qt_label.grid(row=0, column=5)
		for i in range(len(rows)):			
			itemid_label = tk.Label(inventoryframe, text=rows[i][0])
			itemid_label.grid(row=i+10, column=1)
			laptopname_label = tk.Label(inventoryframe, text=rows[i][1])
			laptopname_label.grid(row=i+10, column=2)
			spec_text = tk.Label(inventoryframe, text=rows[i][2])
			spec_text.grid(row=i+10, column=3)
			pricelabel = tk.Label(inventoryframe, text=rows[i][3])
			pricelabel.grid(row=i+10, column=4)
			qtylabel = tk.Label(inventoryframe, text=rows[i][4])
			qtylabel.grid(row=i+10, column=5)
			
