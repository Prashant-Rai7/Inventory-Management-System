from cgitb import text
from email.mime import image
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class CategoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #============Variables==========
        self.var_category_id=StringVar()
        self.var_category_name=StringVar()


        # ---------title and header---------
        title = Label(self.root, text="Manage Product Category", font=("goudy old style",30,"bold"), bg='#9819fa', fg="white",bd=3, relief=RIDGE    ).pack(side=TOP, padx=10, pady=20,fill=X)

        #----------content---------------
        lbl_enter_category_name = Label(self.root, text="Enter Category Name", font=("goudy old style",30), bg='white').place(x=50,y=100)
        txt_enter_category_name = Entry(self.root,textvariable=self.var_category_name,font=("goudy old style",18), bg='lightyellow').place(x=50,y=170)

        #----------Button------------
        btn_add = Button(self.root,text="ADD",font=("goudy old style",15,"bold  "), bg='#2dfa16',fg="white",cursor="hand2",command=self.add).place(x=360,y=170,width=150,height=30)
        btn_delete = Button(self.root,text="DELETE",font=("goudy old style",15,"bold  "), bg='red',fg="white",cursor="hand2",command=self.delete).place(x=520,y=170,width=150,height=30)

        # ---------Category Details Data---------
        category_frame = Frame(self.root, bd=3, relief=RIDGE)
        category_frame.place(x=700, y=100, width=380, height=100)

        scrolly = Scrollbar(category_frame, orient=VERTICAL)
        scrollx = Scrollbar(category_frame, orient=HORIZONTAL)

        self.category_Table = ttk.Treeview(category_frame, columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category_Table.xview)
        scrolly.config(command=self.category_Table.yview)

        self.category_Table.heading("cid", text="Category ID")
        self.category_Table.heading("name", text="Name")

        self.category_Table["show"] = "headings"

        self.category_Table.column("cid", width=90)
        self.category_Table.column("name", width=100)
        self.category_Table.pack(fill=BOTH, expand=1)
        self.category_Table.bind("<ButtonRelease->", self.get_data)

        self.show()

        #---------Images1------------
        self.img1=Image.open("Stock Images/cat.jpg")
        self.img1=self.img1.resize((500,250),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(self.img1)

        self.lbl_img1=Label(self.root,image=self.img1,bd=2,relief=RAISED)
        self.lbl_img1.place(x=50,y=220)

        #---------Images2------------
        self.img2=Image.open("Stock Images/category.jpg")
        self.img2=self.img2.resize((500,250),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(self.img2)

        self.lbl_img2=Label(self.root,image=self.img2,bd=2,relief=RAISED)
        self.lbl_img2.place(x=575,y=220)
    

    # ----------------ADD BUTTON Functionality----------------
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_category_name.get() == "":
                messagebox.showerror("Error", "Category Name is required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_category_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Category is already present, try different one")
                else:
                    cur.execute("Insert into category (name) values(?)", (self.var_category_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    # ========show data==========
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.category_Table.delete(*self.category_Table.get_children())
            for row in rows:
                self.category_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # ========show data in Both==========
    def get_data(self, ev):
        f = self.category_Table.focus()
        content = (self.category_Table.item(f))
        row = content['values']
        # print(row)
        self.var_category_id.set(row[0])
        self.var_category_name.set(row[1])

# ----------------DELETE BUTTON Functionality----------------

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_category_id.get() == "":
                messagebox.showerror("Error", "Please select category from the list", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_category_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Try Again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?",(self.var_category_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)

                        self.show()
                        self.var_category_id.set("")
                        self.var_category_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

if __name__ == "__main__":

    root = Tk()
    obj = CategoryClass(root)
    root.mainloop()
