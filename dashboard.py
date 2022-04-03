from tkinter import*
from PIL import Image,ImageTk
from employee import EmployeeClass
from supplier import SupplierClass
from category import CategoryClass
from product  import ProductClass
from sales import SalesClass
import os

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #----------Title and Header 1-------------
        self.icon_cart=PhotoImage(file="Stock Images/logo1.png")
        lbl_title=Label(self.root,image=self.icon_cart,compound=LEFT,padx=30,text="Inventory Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w").place(x=0,y=0,height=70,relwidth=1)
        btn_logout=Button(root,command=self.logout,text="Logout",font=("Imperial",15,"bold"),bd=5,relief=RIDGE,cursor='hand2',bg='yellow').place(x=1200,y=15,height=40, width=100)
        
        #----------Title and Header 2-------------
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t\tDate : DD-MM-YYYY\t\t\tTime :HH:MM:SS",font=("goudy old style",15,"bold"),bg="#a200ff",fg="white").place(x=0,y=70,height=30,relwidth=1)

        #----------Left Menu Frame-------------
        self.left_icon=Image.open("Stock Images/menu_im.png")
        self.left_icon=self.left_icon.resize((200,200),Image.ANTIALIAS)
        self.left_icon=ImageTk.PhotoImage(self.left_icon)
        left_menu=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        left_menu.place(x=0,y=100,width=200,height=565)

        lbl_left_icon=Label(left_menu,image=self.left_icon)
        lbl_left_icon.pack(side=TOP,fill=X)

        #-------------BUTTON & LABEL-------------
        lbl_menu=Label(left_menu,text="Menu",font=("times new roman",20),bg="#02c262").pack(side=TOP,fill=X)
        self.icon_side=PhotoImage(file="Stock Images/side.png")
        btn_employee=Button(left_menu,image=self.icon_side,compound=LEFT,padx=5,anchor="w",text="Employee",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2",command=self.employee).pack(side=TOP,fill=X)
        btn_supplier=Button(left_menu,image=self.icon_side,compound=LEFT,padx=5,anchor="w",text="Supplier",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2",command=self.supplier).pack(side=TOP,fill=X)
        btn_category=Button(left_menu,image=self.icon_side,compound=LEFT,padx=5,anchor="w",text="Category",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2",command=self.category  ).pack(side=TOP,fill=X)
        btn_product=Button(left_menu,image=self.icon_side,compound=LEFT,padx=5,anchor="w",text="Products",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2",command=self.product).pack(side=TOP,fill=X)
        btn_sales=Button(left_menu,image=self.icon_side,compound=LEFT,padx=5,anchor="w",text="Sales",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2",command=self.sales).pack(side=TOP,fill=X)
        btn_exit=Button(left_menu,image=self.icon_side,compound=LEFT,padx=5,anchor="w",text="Exit",font=("times new roman",20,"bold"),bd=3,bg="white",cursor="hand2",command=self.exit).pack(side=TOP,fill=X)

        #------------Content and Dashboard-------------
        self.lbl_employee_block=Label(self.root,text="Total Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee_block.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier_block=Label(self.root,text="Total Suppplier\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier_block.place(x=650,y=120,height=150,width=300)

        self.lbl_category_block=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#2aff12",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category_block.place(x=1000,y=120,height=150,width=300)

        self.lbl_product_block=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product_block.place(x=300,y=300,height=150,width=300)

        self.lbl_sales_block=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales_block.place(x=650,y=300,height=150,width=300)

        #------------Footer--------------
        self.lbl_footer=Label(self.root,text="All Rights Reserved | Developed by Prashant Rai",font=("goudy old style",12,"bold"),bg="#a200ff",fg="white").pack(side=BOTTOM,fill=X)

    #===============================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=EmployeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CategoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProductClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win)
        
    def exit(self):
        self.root.destroy()
        
    def logout(self):
        self.root.destroy()
        os.system("python Dashboard/login.py")


if __name__=="__main__":

    root=Tk()
    obj=IMS(root)
    root.mainloop()