from cgitb import text
from tkinter import*
from turtle import width
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #-------------Variables---------------
        self.var_pid = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.cat_List=[]
        self.sup_List=[]
        self.fetch_cat_sup()

        #--------Frames------------
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")     
        product_Frame.place(x=10,y=10,width=450, height=480)
        
        # ---------Title and header---------
        title = Label(product_Frame, text="Manage Product Details", font=("goudy old style", 20,"bold"), bg='#59ff00', fg="white").pack(side=TOP,fill=X)

        # ------------Content--------------
        #======Column 1======
        lbl_category = Label(product_Frame, text="Category", font=("goudy old style", 15), bg="white").place(x=30, y=60)
        lbl_supplier= Label(product_Frame, text="Supplier", font=("goudy old style", 15), bg="white").place(x=30, y=110)
        lbl_name = Label(product_Frame, text="Name", font=("goudy old style", 15), bg="white").place(x=30, y=160)
        lbl_price = Label(product_Frame, text="Price", font=("goudy old style", 15), bg="white").place(x=30, y=210)
        lbl_quantity = Label(product_Frame, text="Quantity", font=("goudy old style", 15), bg="white").place(x=30, y=260)
        lbl_status = Label(product_Frame, text="Status", font=("goudy old style", 15), bg="white").place(x=30, y=310)

        #======Column 2======
        cmb_category = ttk.Combobox(product_Frame, textvariable=self.var_category, values=self.cat_List, stat="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_category.place(x=150, y=60,width=200)
        cmb_category.current(0)

        cmb_supplier = ttk.Combobox(product_Frame, textvariable=self.var_supplier, values=self.sup_List, stat="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_supplier.place(x=150, y=110,width=200)
        cmb_supplier.current(0)

        txt_name = Entry(product_Frame,textvariable=self.var_name, font=("goudy old style", 15), bg="#fff382").place(x=150, y=160)
        txt_price = Entry(product_Frame,textvariable=self.var_price, font=("goudy old style", 15), bg="#fff382").place(x=150, y=210)
        txt_quantity = Entry(product_Frame,textvariable=self.var_quantity, font=("goudy old style", 15), bg="#fff382").place(x=150, y=260)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active","Inactive"), stat="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=310,width=200)
        cmb_status.current(0)

        # ===========Buttons===========
        btn_save = Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15,"bold"),bg='#2196f3', fg="white", cursor="hand2").place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=("goudy old style", 15,"bold"), bg='#ffc400',fg="white", cursor="hand2").place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete, font=("goudy old style", 15,"bold"), bg='red',fg="white", cursor="hand2").place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=("goudy old style", 15,"bold"), bg='#6b0db8',fg="white", cursor="hand2").place(x=340, y=400, width=100, height=40)

        # ----------search product frames------------
        search_frame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=480, y=10, width=600, height=80)

        # ----------option--------------
        cmb_search = ttk.Combobox(search_frame, textvariable=self.var_searchby, values=("select", "Category", "Supplier", "Name"), stat="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(search_frame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg='#fff382').place(x=200, y=11)
        btn_search = Button(search_frame, text="Search", command=self.search, font=("goudy old style", 15,"bold"),bg='#409100', fg="white", cursor="hand2").place(x=435, y=9, width=150, height=30)


        # ---------Product Details Data---------
        product_frame = Frame(self.root, bd=3, relief=RIDGE)
        product_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(product_frame, columns=("pid", "category", "supplier", "name", "price", "qty", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="Prod ID")
        self.product_Table.heading("category", text="Category")
        self.product_Table.heading("supplier", text="Supplier")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="QTY")
        self.product_Table.heading("status", text="Status")

        self.product_Table["show"] = "headings"

        self.product_Table.column("pid", width=90)
        self.product_Table.column("category", width=100)
        self.product_Table.column("supplier", width=100)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=100)
        self.product_Table.column("status", width=100)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease->", self.get_data)

        self.show()
    # ----------------SAVE BUTTON Functionality----------------
    def fetch_cat_sup(self):
        self.cat_List.append("Empty")
        self.sup_List.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()

            if len(cat)>0:
                del self.cat_List[:]
                self.cat_List.append("select")
                for i in cat:
                    self.cat_List.append(i[0])  

            cur.execute("Select name from supplier")
            sup=cur.fetchall()

            if len(sup)>0:
                del self.sup_List[:]
                self.sup_List.append("select")
                for i in sup:
                    self.sup_List.append(i[0]) 

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
        
            if self.var_category.get() == "select" or self.var_category.get() == "Empty" or self.var_supplier.get() == "select" or self.var_supplier.get() == "Empty" or self.var_name.get()=="" or self.var_price.get()=="" or self.var_quantity.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Product is already present, try different one")
                else:
                    cur.execute("Insert into product (category,supplier,name,price,qty,status) values(?,?,?,?,?,?)", (
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    # ========show data==========
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # ========show data in Both==========
    def get_data(self, ev):
        f = self.product_Table.focus()
        content = (self.product_Table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_category.set(row[1])
        self.var_supplier.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])

# ----------------UPDATE BUTTON Functionality----------------
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please Select Product from List", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    cur.execute("Update product set category=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?", (

                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                con.commit()
                messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


# ----------------DELETE BUTTON Functionality----------------

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select product from list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

# ----------------CLEAR BUTTON Functionality----------------
    def clear(self):
        self.var_category.set("select"),
        self.var_supplier.set("select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_quantity.set(""),
        self.var_status.set("Active"),
        self.var_pid.set(""),
        self.var_searchtxt.set("")
        self.var_searchby.set("select")
        self.show()

    # -----------------search bar at TOP--------------------
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "select":
                messagebox.showerror("Error", "Please select Search by option given", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("Select * from product where " +self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)










if __name__ == "__main__":

    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
