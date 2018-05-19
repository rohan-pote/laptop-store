# Name: Rohan Pote
# Final project
# Pyhton 2

import Tkinter as tk
import sqlite3
from admin import *
import random
from random import randint
import tkMessageBox


# ----------------- Function to create an order -----------------
def create_order(userid):
	myapp = tk.Tk()
	myapp.geometry("1366x768")
	myapp.title("Create an Order")
	
	inventoryframe = tk.Frame(myapp)
	inventoryframe.pack()
	
	
	with sqlite3.connect("finalproject.db") as conn:
		result = conn.execute("select * from inventory")
		rows = result.fetchall()
		for i in range(len(rows)):
			#select_cb = tk.Checkbutton(inventoryframe)
			#select_cb.grid(row=i, column=1)
			
			item_label = tk.Label(inventoryframe, text="Product ID", bg="light blue", width=20, borderwidth=1, relief="solid")
			lp_label = tk.Label(inventoryframe, text = "Laptop Name", bg="light blue", width=30, borderwidth=1, relief="solid")
			sp_label = tk.Label(inventoryframe, text="Specifications", bg="light blue", width=30, borderwidth=1, relief="solid")
			pr_label = tk.Label(inventoryframe, text="Price", bg="light blue", width=10, borderwidth=1, relief="solid")
			qt_label = tk.Label(inventoryframe, text="Quantity", bg="light blue", width = 10, borderwidth=1, relief="solid")
			item_label.grid(row=0, column=1)
			lp_label.grid(row=0, column=2)
			sp_label.grid(row=0, column=3)
			pr_label.grid(row=0, column=4)
			qt_label.grid(row=0, column=5)
			
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
			
		item_label = tk.Label(inventoryframe, text="Enter the Product ID: ")
		item_label.grid(row=50, column=1)
		item_entry = tk.Entry(inventoryframe)
		item_entry.grid(row=50, column=2)
		qty_label = tk.Label(inventoryframe, text="Quantity: ")
		qty_label.grid(row=70, column=1)
		qty_box = tk.Spinbox(inventoryframe, from_=0,to=10, width=5)
		qty_box.grid(row=70, column=2)
		add_button = tk.Button(inventoryframe, text="Add to cart", command=lambda: add_to_cart(item_entry.get(), qty_box.get(), userid))
		add_button.grid(row=150, column=1)
		viewcart_button = tk.Button(inventoryframe, text="View Cart", command=lambda: view_cart(userid))
		viewcart_button.grid(row=150, column=2)
		
		
				
			
			
	
# ---------------------- Functon to add the created order to the cart -------------
def add_to_cart(itemid, qty, userid):
	ordernumber = range(0,1000)
	with sqlite3.connect("finalproject.db") as conn:
		result = conn.execute("select * from inventory where item_id=?", (itemid,))
		for rows in result.fetchall():
			item,lpname,sp,price,quant=rows
			if quant == 0:
				tkMessageBox.showinfo("Sorry!", "This product is sold out!")
			elif (int(qty) > int(quant)):
				tkMessageBox.showinfo("Sorry!", "Selected quantity not available")
			else:	
				totalprice = int(price)*int(qty)
				newquantity = int(quant) - int(qty)
				conn.execute("insert into cartdata values (?,?,?,?,?,?)", (ordernumber[randint(0,1000)], userid, item, lpname, qty, totalprice))
				tkMessageBox.showinfo("Success!", "Product added to cart")
				conn.execute("update inventory set quantity=? where item_id=?", (newquantity, itemid))	
		
		
#----- Function to display the items in cart for the user ---- 
def view_cart(userid):
	myapp = tk.Tk()
	myapp.geometry("1366x768")
	myapp.title("Your Cart")
	
	cartframe = tk.Frame(myapp)
	cartframe.pack()
	
	with sqlite3.connect("finalproject.db") as conn:
		result = conn.execute("select * from cartdata where uname=?", (userid,))
		rows = result.fetchall()
		for i in range(len(rows)):
			#ordernum,lname,price,qt,uname,item=rows
			order_label = tk.Label(cartframe, text="Order Number", bg="light blue", width=20, borderwidth=1, relief="solid")
			lp_label = tk.Label(cartframe, text = "Username", bg="light blue", width=20, borderwidth=1, relief="solid")
			pr_label = tk.Label(cartframe, text="Product ID", bg="light blue", width=20, borderwidth=1, relief="solid")
			q_label = tk.Label(cartframe, text="Laptop Name", bg="light blue", width=20, borderwidth=1, relief="solid")
			u_label = tk.Label(cartframe, text="Quantity", bg="light blue", width=20, borderwidth=1, relief="solid")
			itemid_label = tk.Label(cartframe, text="Price", bg="light blue", width=20, borderwidth=1, relief="solid")
			order_label.grid(row=0, column=1)
			lp_label.grid(row=0, column=2)
			pr_label.grid(row=0, column=3)
			q_label.grid(row=0, column=4)
			u_label.grid(row=0, column=5)
			itemid_label.grid(row=0, column=6)
			
			ordernum_label = tk.Label(cartframe, text=rows[i][0])
			lname_label = tk.Label(cartframe, text=rows[i][1])
			price_label = tk.Label(cartframe, text=rows[i][2])
			qt_label = tk.Label(cartframe, text=rows[i][3])
			uname_label = tk.Label(cartframe, text=rows[i][4])
			item_label = tk.Label(cartframe, text=rows[i][5])
			
			ordernum_label.grid(row=i+10, column=1)
			lname_label.grid(row=i+10, column=2)
			price_label.grid(row=i+10, column=3)
			qt_label.grid(row=i+10, column=4)
			uname_label.grid(row=i+10, column=5)
			item_label.grid(row=i+10, column=6)
			
		grand_total = tk.Label(cartframe, text="Grand Total = ", bg="light blue", width=20, borderwidth=1, relief="solid", font="Calibri 10 bold")
		grand_total.grid(row=100, column=5)
		
		with sqlite3.connect("finalproject.db") as conn:
			result = conn.execute("select sum(price) from cartdata where uname=?", (userid,))
			grand_total = result.fetchone()
			grand_total_label = tk.Label(cartframe, text=grand_total, bg="light blue", width=20, borderwidth=1, relief="solid", font="Calibri 10 bold")
			grand_total_label.grid(row=100, column=6)
		
		
				
				
	
		
		
		
# -----------------GUI for modification of existing order ----------------- 	
def modify_order():
	myapp = tk.Tk()
	myapp.geometry("1366x768")
	myapp.title("Modify an Order")
	order_num_label = tk.Label(myapp, text="Enter order number you want to modify: ")
	order_num_label.place(x=100, y=50)
	order_num_entry = tk.Entry(myapp)
	order_num_entry.place(x=350, y=50)
	#modify_item = tk.Label(myapp, text="Enter the Item ID : ")
	#modify_item.place(x=100, y=75)
	#modify_item_entry = tk.Entry(myapp)
	#modify_item_entry.place(x=350, y=75)
	modify_label = tk.Label(myapp, text="Enter the quantity: ")
	modify_label.place(x=100, y=100)
	modify_qty = tk.Spinbox(myapp, from_=0,to=100, width=5)
	modify_qty.place(x=350, y=100)
	modify_button = tk.Button(myapp, text="Modify", command=lambda: modify_cart(int(order_num_entry.get()), modify_qty.get()))
	modify_button.place(x=100, y=150)
	

	
# -------------- Function to update modified order in the database -------------------	
def modify_cart(num, qty):
	with sqlite3.connect("finalproject.db") as conn:
		result = conn.execute("select * from cartdata where ordernumber=?", (num,))
		row = result.fetchone()
		if row == None:
			tkMessageBox.showinfo(" ", "This order does not exist!")
		else:
			result = conn.execute("select * from cartdata where ordernumber=?", (num,))
			for rows in result.fetchall():
				order,uname,itemid,lpname,quant,price=rows
			rslt = conn.execute("select * from inventory where item_id=?", (itemid,))
			for i in rslt.fetchall():
				item_id,lpnme,spec,pr,qtt=i
				if(int(qty) > int(qtt)):
					tkMessageBox.showinfo("Sorry!", "Select quantity not available!")
				elif (int(qty) > int(quant)):
					newquantity = (int(qtt) - (int(qty)-int(quant)))
					conn.execute("update inventory set quantity=? where item_id=?", (newquantity, itemid))
					newprice = int(pr)*int(qty)
					conn.execute("update cartdata set quantity=? where ordernumber=?", (qty, num))
					conn.execute("update cartdata set price=? where ordernumber=?", (newprice, num))
					tkMessageBox.showinfo("Success!", "Order modified successfully!")
				elif (int(quant) > int(qty)):
					newquantity = (int(qtt) + (int(quant)-int(qty)))
					conn.execute("update inventory set quantity=? where item_id=?", (newquantity, itemid))
					newprice = int(pr)*int(qty)
					conn.execute("update cartdata set quantity=? where ordernumber=?", (qty, num))
					conn.execute("update cartdata set price=? where ordernumber=?", (newprice, num))
					tkMessageBox.showinfo("Success!", "Order modified successfully!")
					
					
			
		
		
#-------------- GUI for deletion of an order -----------------		
def delete_order():
	myapp = tk.Tk()
	myapp.geometry("1366x768")
	myapp.title("Delete an Order")
	
	order_num_label = tk.Label(myapp, text="Enter order number you want to delete: ")
	order_num_label.place(x=100, y=50)
	order_num_entry = tk.Entry(myapp)
	order_num_entry.place(x=350, y=50)
	modify_button = tk.Button(myapp, text="Delete", command=lambda: delete_from_cart(order_num_entry.get()))
	modify_button.place(x=100, y=100)
	

# -------------- Function to delete an order from database ------------
def delete_from_cart(ornumber):
	with sqlite3.connect("finalproject.db") as conn:
		search = conn.execute("select * from cartdata where ordernumber=?", (ornumber,))
		row = search.fetchall()
		if row == None:
			tkMessageBox.showinfo("Incorrect!", "This order does not exist")
		else:
			conn.execute("delete from cartdata where ordernumber=?", (ornumber,))
			tkMessageBox.showinfo("Success!", "Order removed successfully")
		for i in row:
			ornum,uname,itemid,laptop,qty,price=i
			x = conn.execute("select quantity from inventory where item_id=?", (itemid))
			z = x.fetchone()
			newqty = int(z) + int(qty)
			conn.execute("update inventory set quantity=? where item_id=?", (newqty, itemid))

			

		
	