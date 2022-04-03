from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #===========variables============

        #----------Title and Header 1-------------
        self.icon_cart=PhotoImage(file="Stock Images/logo1.png")
        lbl_title=Label(self.root,image=self.icon_cart,compound=LEFT,padx=30,text="Inventory Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w").place(x=0,y=0,height=70,relwidth=1)
        btn_logout=Button(root,command=self.logout,text="Logout",font=("Imperial",15,"bold"),bd=5,relief=RIDGE,cursor='hand2',bg='yellow').place(x=1200,y=15,height=40, width=100)
        
        #----------Title and Header 2-------------
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t\tDate : DD-MM-YYYY\t\t\tTime :HH:MM:SS",font=("goudy old style",15,"bold"),bg="#a200ff",fg="white").place(x=0,y=70,height=30,relwidth=1)

        #---------------------Product Main Frame----------------------------

        #==============All Product Frame=============
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        #============Product Search and Name Frame==============
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        self.var_search=StringVar()

        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15),bg="white",fg="green").place(x=2,y=5)
        lbl_name=Label(ProductFrame2,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=45)
        txt_name=Entry(ProductFrame2,textvariable=self.var_search ,font=("times new roman",15),bg="lightyellow").place(x=130,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2",bd=2).place(x=286, y=45, width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2",bd=2).place(x=286, y=10, width=100,height=25)

        #===================Product Details Side Bar Frame==================== 
        ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2, y=140, width=398, height=385)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="PID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="QTY")
        self.product_Table.heading("status", text="Status")

        self.product_Table["show"] = "headings"

        self.product_Table.column("pid", width=90)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=100)
        self.product_Table.column("status", width=100)
        self.product_Table.pack(fill=BOTH, expand=1)
        # self.product_Table.bind("<ButtonRelease->", self.get_data)
        lbl_note=Label(ProductFrame1, text="Note:   Enter 0 Quantity to remove product from the cart",font=("goudy old style",10,'bold'),anchor=W ,bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #========================Customer Frame=========================
        self.var_customer_name=StringVar()
        self.var_phone=StringVar()
        self.var_contact=StringVar()

        #==============Customer Name and Contact Frame=============
        Customer_Details_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Customer_Details_Frame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(Customer_Details_Frame,text="Customers Details",font=("goudy old style",15),bg="Lightgrey").pack(side=TOP,fill=X)
        lbl_c_name=Label(Customer_Details_Frame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_c_name=Entry(Customer_Details_Frame,textvariable=self.var_customer_name ,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_c_phone=Label(Customer_Details_Frame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_c_phone=Entry(Customer_Details_Frame,textvariable=self.var_phone ,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

        #==============Calculator and Side Bar containing frame=============
        Calc_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Calc_Cart_Frame.place(x=420,y=190,width=530,height=360)


        #===========================Calculator Frame=============================

        self.var_calc_input=StringVar()

        Calc_Frame=Frame(Calc_Cart_Frame,bd=8,relief=RIDGE,bg="white")
        Calc_Frame.place(x=5,y=10,width=268,height=340)

        self.txt_calc_input=Entry(Calc_Frame,textvariable=self.var_calc_input, font=("arial",15,"bold"),width=21, bd=10, relief=GROOVE,state='readonly',justify=RIGHT)
        self.txt_calc_input.grid(row=0,columnspan=4)

        btn_7=Button(Calc_Frame,text='7',command=lambda:self.get_input(7) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(Calc_Frame,text='8',command=lambda:self.get_input(8) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=1,column=1)
        btn_9=Button(Calc_Frame,text='9',command=lambda:self.get_input(9) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=1,column=2)
        btn_plus=Button(Calc_Frame,text='+',command=lambda:self.get_input("+") ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=1,column=3)

        btn_4=Button(Calc_Frame,text='4',command=lambda:self.get_input(4) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=2,column=0)
        btn_5=Button(Calc_Frame,text='5',command=lambda:self.get_input(5) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=2,column=1)
        btn_6=Button(Calc_Frame,text='6',command=lambda:self.get_input(6) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=2,column=2)
        btn_minus=Button(Calc_Frame,text='-',command=lambda:self.get_input("-") ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=2,column=3)

        btn_1=Button(Calc_Frame,text='1',command=lambda:self.get_input(1) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=3,column=0)
        btn_2=Button(Calc_Frame,text='2',command=lambda:self.get_input(2) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=3,column=1)
        btn_3=Button(Calc_Frame,text='3',command=lambda:self.get_input(3) ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=3,column=2)
        btn_mult=Button(Calc_Frame,text='x',command=lambda:self.get_input("*") ,font=("arial",15,"bold"),bd=5, width=4,pady=10,cursor='hand2').grid(row=3,column=3)

        btn_clear=Button(Calc_Frame,text='C',command=self.clear_calc ,font=("arial",15,"bold"),bd=5, width=4,pady=15,cursor='hand2').grid(row=4,column=0)
        btn_zero=Button(Calc_Frame,text='00',command=lambda:self.get_input(00) ,font=("arial",15,"bold"),bd=5, width=4,pady=15,cursor='hand2').grid(row=4,column=1)
        btn_equal=Button(Calc_Frame,text='=',command=self.perform_calc ,font=("arial",15,"bold"),bd=5, width=4,pady=15,cursor='hand2').grid(row=4,column=2)
        btn_divison=Button(Calc_Frame,text='/',command=lambda:self.get_input("/") ,font=("arial",15,"bold"),bd=5, width=4,pady=15,cursor='hand2').grid(row=4,column=3)




        #========================Calculator Side Bar Frame=========================
        CART_Frame = Frame(Calc_Cart_Frame, bd=3, relief=RIDGE)
        CART_Frame.place(x=280, y=8, width=245, height=342)
        cart_Title=Label(CART_Frame,text="Cart\tTotal Product: [0]",font=("times new roman",15),bg="Lightgrey").pack(side=TOP,fill=X)

        scrolly = Scrollbar(CART_Frame, orient=VERTICAL)
        scrollx = Scrollbar(CART_Frame, orient=HORIZONTAL)

        self.cart_Table = ttk.Treeview(CART_Frame, columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)

        self.cart_Table.heading("pid", text="PID")
        self.cart_Table.heading("name", text="Name")
        self.cart_Table.heading("price", text="Price")
        self.cart_Table.heading("qty", text="QTY")
        self.cart_Table.heading("status", text="Status")

        self.cart_Table["show"] = "headings"

        self.cart_Table.column("pid", width=40)
        self.cart_Table.column("name", width=100)
        self.cart_Table.column("price", width=90)
        self.cart_Table.column("qty", width=40)
        self.cart_Table.column("status", width=90)
        self.cart_Table.pack(fill=BOTH, expand=1)
        # self.cart_Table.bind("<ButtonRelease->", self.get_data)

        #==============Add Cart Widgets Frame=============
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_cart_widgets_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_cart_widgets_Frame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_cart_widgets_Frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_cart_widgets_Frame,textvariable=self.var_pname,font=("times new roman",15),state="readonly",bg="lightyellow").place(x=5,y=35,height=22,width=190)

        lbl_p_price=Label(Add_cart_widgets_Frame,text="Price Per QTY",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_cart_widgets_Frame,textvariable=self.var_price,font=("times new roman",15),state="readonly",bg="lightyellow").place(x=230,y=35,height=22,width=150)

        lbl_p_qty=Label(Add_cart_widgets_Frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_cart_widgets_Frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=395,y=35,height=22,width=120)

        self.lbl_inStock=Label(Add_cart_widgets_Frame,text="In Stock [9999]",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        btn_clear_cart=Button(Add_cart_widgets_Frame,text="Clear",font=("goudy old style",15,"bold"),bg="lightgrey",cursor="hand2",bd=3).place(x=180, y=70, width=150,height=30)
        btn_add_cart=Button(Add_cart_widgets_Frame,text="Add | Update Cart",font=("goudy old style",15,"bold"),bg="orange",cursor="hand2",bd=3).place(x=340, y=70, width=180,height=30)


        #============== BILLING AREA Frame =============
        self.txt_bill_area=StringVar()
        Bill_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Bill_Frame.place(x=953,y=110,width=410,height=410)

        b_Title=Label(Bill_Frame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="red",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(Bill_Frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.txt_bill_area=Text(Bill_Frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #========================= Billing Button ============================

        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=410,height=140)

        self.lbl_amount=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#290f4a",fg="white")
        self.lbl_amount.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(billMenuFrame,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg="#88ff00",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#ff0853",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)


        btn_print=Button(billMenuFrame,text="Print",font=("goudy old style",15,"bold"),bg="#3d6613",fg="white",cursor="hand2")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(billMenuFrame,text="Clear All",font=("goudy old style",15,"bold"),bg="#154347",fg="white",cursor="hand2")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(billMenuFrame,text="Generate Bill",font=("goudy old style",15,"bold"),bg="#ffcd03",fg="white",cursor="hand2")
        btn_generate.place(x=246,y=80,width=160,height=50)


        #============================Footer=================================
        lbl_footer=Label(self.root,text="All Rights Reserved | Developed by Prashant Rai",font=("goudy old style",12,"bold"),bg="#a200ff",fg="white").pack(side=BOTTOM,fill=X)
        self.show()





    #====================================== All Functions =========================================

    def get_input(self,num):
        xnum=self.var_calc_input.get()+str(num)
        self.var_calc_input.set(xnum)

    def clear_calc(self):
        self.var_calc_input.set('')
    
    def perform_calc(self):
        result=self.var_calc_input.get()
        self.var_calc_input.set(eval(result))


    # ========show data==========
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            # self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python Dashboard/login.py")

if __name__=="__main__":

    root=Tk()
    obj=BillClass(root)
    root.mainloop()