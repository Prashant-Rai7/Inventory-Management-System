from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

# ==================================================================
        # All Variables
        self.var_searchtxt = StringVar()

        self.var_supp_invoice_no = StringVar()
        self.var_supp_name = StringVar()
        self.var_supp_contact = StringVar()

# ==================================================================
        # ---------title and header---------
        title = Label(self.root, text="Supplier Details", font=("goudy old style",20,"bold"), bg='#7b27a8', fg="white").place(x=50, y=10, width=1000,height=40)

        # --------------content-----------------
        lbl_supplier_invoice_no = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg='white').place(x=50, y=80)
        lbl_supplier_name = Label(self.root, text="Name", font=("goudy old style", 15), bg='white').place(x=50, y=120)
        lbl_supplier_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg='white').place(x=50, y=160)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15), bg='white').place(x=50, y=200)

        txt_supplier_invoice_no = Entry(self.root, textvariable=self.var_supp_invoice_no, font=("goudy old style", 15), bg='lightyellow').place(x=180, y=80, width=180)
        txt_supplier_name = Entry(self.root, textvariable=self.var_supp_name, font=("goudy old style", 15), bg='lightyellow').place(x=180, y=120, width=180)
        txt_supplier_contact = Entry(self.root, textvariable=self.var_supp_contact, font=("goudy old style", 15), bg='lightyellow').place(x=180, y=160, width=180)
        self.txt_description = Text(self.root, font=("goudy old style", 15), bg='lightyellow')
        self.txt_description.place(x=180, y=200, width=470, height=120)

        # ===========Buttons===========
        btn_save = Button(self.root, text="Save", command=self.save, font=("goudy old style", 15,"bold"),bg='#2196f3', fg="white", cursor="hand2").place(x=180, y=370, width=110, height=35)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15,"bold"), bg='#2dfa16',fg="white", cursor="hand2").place(x=300, y=370, width=110, height=35)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15,"bold"), bg='red',fg="white", cursor="hand2").place(x=420, y=370, width=110, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15,"bold"), bg='#607d8b',fg="white", cursor="hand2").place(x=540, y=370, width=110, height=35)

        # ----------search frames------------

        # ----------option--------------
        lbl_search = Label(self.root,text="Invoice No.",font=("goudy old style", 15))
        lbl_search.place(x=700, y=80)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg='lightyellow').place(x=810, y=80,width=160)
        btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15),bg='#4caf50', fg="white", cursor="hand2").place(x=980, y=79, width=100, height=28)

       

        # ---------Supplier Details Data---------
        supp_frame = Frame(self.root, bd=3, relief=RIDGE)
        supp_frame.place(x=700, y=120, width=380, height=350)

        scrolly = Scrollbar(supp_frame, orient=VERTICAL)
        scrollx = Scrollbar(supp_frame, orient=HORIZONTAL)

        self.Supplier_Table = ttk.Treeview(supp_frame, columns=("invoice","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Supplier_Table.xview)
        scrolly.config(command=self.Supplier_Table.yview)

        self.Supplier_Table.heading("invoice", text="Invoice No.")
        self.Supplier_Table.heading("name", text="Name")
        self.Supplier_Table.heading("contact", text="Contact")
        self.Supplier_Table.heading("description", text="Description")

        self.Supplier_Table["show"] = "headings"

        self.Supplier_Table.column("invoice", width=90)
        self.Supplier_Table.column("name", width=100)
        self.Supplier_Table.column("contact", width=100)
        self.Supplier_Table.column("description", width=100)
        self.Supplier_Table.pack(fill=BOTH, expand=1)
        self.Supplier_Table.bind("<ButtonRelease->", self.get_data)

        self.show()

    # ----------------SAVE BUTTON Functionality----------------
    def save(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_supp_invoice_no.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_supp_invoice_no.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Invoice No. already assigned, Please try different one")
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,description) values(?,?,?,?)", (
                        self.var_supp_invoice_no.get(),
                        self.var_supp_name.get(),
                        self.var_supp_contact.get(),
                        self.txt_description.get('1.0', END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    # ========show data==========
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.Supplier_Table.delete(*self.Supplier_Table.get_children())
            for row in rows:
                self.Supplier_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # ========show data in Both==========
    def get_data(self, ev):
        f = self.Supplier_Table.focus()
        content = (self.Supplier_Table.item(f))
        row = content['values']
        # print(row)
        self.var_supp_invoice_no.set(row[0])
        self.var_supp_name.set(row[1])
        self.var_supp_contact.set(row[2])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[3])

# ----------------UPDATE BUTTON Functionality----------------
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_supp_invoice_no.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_supp_invoice_no.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,description=? where invoice=?", (

                        self.var_supp_name.get(),   
                        self.var_supp_contact.get(),
                        self.txt_description.get('1.0', END),
                        self.var_supp_invoice_no.get(),
                    ))
                con.commit()
                messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)

                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


# ----------------DELETE BUTTON Functionality----------------

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_supp_invoice_no.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_supp_invoice_no.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice=?",(self.var_supp_invoice_no.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)

                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

# ----------------CLEAR BUTTON Functionality----------------
    def clear(self):
        self.var_supp_invoice_no.set("")
        self.var_supp_name.set("")
        self.var_supp_contact.set("")
        self.txt_description.delete('1.0', END)
        self.var_searchtxt.set("")

        self.show()

    # -----------------search bar at TOP--------------------
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice No. should be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.Supplier_Table.delete(*self.Supplier_Table.get_children())
                    self.Supplier_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":

    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
