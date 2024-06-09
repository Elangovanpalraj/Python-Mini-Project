# LIBRARY MANAGEMENT SYSTEM
# -------------------------

from tkinter import *
from tkinter import ttk
#import mysql.connector as mc
import tkinter.messagebox as tm
from PIL import ImageTk, Image
import random
import sqlite3

# image1='library.png'
# image2
# image3='image3.png'
def createnewwindow():
        root1 = Tk()
        root1.state('zoomed') 
        root1.config(bg='green')
        root1.title("LIBRARY MANAGEMANT SYSTEM")
        #root1.canvases(image1)
        l1=Button(root1,text='BOOK DATA',command = book,font='Papyrus 22 bold',fg='Yellow',bg='Black',width=19,padx=10,borderwidth=0).place(x=100,y=500)
        l2=Button(root1,text='STUDENT DATA',command =student,font='Papyrus 22 bold',fg='Yellow',bg='Black',width=19,padx=10,borderwidth=0).place(x=800,y=500)

        url = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\image2.png"))# general syntax to open jpeg img
        
        p1 = Label(root1, image = url,height=1000,width=3000)
        p1.pack()
#p1.pack(fill = "both")        
        

def book():
        root2 = Tk()
        root2.state('zoomed') 
        root2.config(bg='yellow')
        root2.title("LIBRARY MANAGEMANT SYSTEM")
        l3=Button(root2,text='Add Books',command=addbook,font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10).place(x=12,y=100)
        l4=Button(root2,text='Search Book',command=search,font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10).place(x=12,y=200)

        l5=Button(root2,text='All Books',command= all,font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10).place(x=12,y=300)
        l6=Button(root2,text='<< Main Menu',command=mainmenu,font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10).place(x=12,y=500)



def addbook():
        root2 = Tk()
        root2.state('zoomed') 
        root2.config(bg='yellow')
        root2.title("LIBRARY MANAGEMANT SYSTEM")
        id=StringVar()
        author=StringVar()
        name=StringVar()
        copies=IntVar()
        genre=StringVar()
        loc=StringVar()
        f1=Frame(root2,height=500,width=650,bg='black')
        f1.place(x=500,y=100)
        l1=Label(f1,text='Book ID : ',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(f1,width=45,bg='orange',fg='black',textvariable=id).place(x=150,y=50)
        l2=Label(f1,text='Title Name : ',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=100)
        e2=Entry(f1,width=45,bg='orange',fg='black',textvariable=name).place(x=150,y=100)
        l3=Label(f1,text='Author : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=150)
        e3=Entry(f1,width=45,bg='orange',fg='black',textvariable=author).place(x=150,y=150)
        l4=Label(f1,text='Genre : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=200)
        e2=Entry(f1,width=45,bg='orange',fg='black',textvariable=genre).place(x=150,y=200)
        l4=Label(f1,text='Copies : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=250)
        e2=Entry(f1,width=45,bg='orange',fg='black',textvariable=copies).place(x=150,y=250)
        l5=Label(f1,text='Location : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=300)
        e3=Entry(f1,width=45,bg='orange',fg='black',textvariable=loc).place(x=150,y=300)
        f1.grid_propagate(0)
        b1=Button(f1,text='Add',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=adddata).place(x=150,y=400)
        b2=Button(f1,text='Back',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=rm).place(x=350,y=400)
def search():
        root2=Tk()
        root2.config(bg='yellow')
        root2.title("LIBRARY MANAGEMANT SYSTEM")
        root2.state('zoomed')
        sid=StringVar()
        f1=Frame(root2,height=500,width=650,bg='black')
        f1.place(x=500,y=100)
        l1=Label(f1,text='Book ID/Title/Author/Genre: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
        e1=Entry(f1,width=25,bd=5,bg='orange',fg='black',textvariable=sid).place(x=260,y=40)
        b1=Button(f1,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=search).place(x=500,y=37)
        b1=Button(f1,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=rm).place(x=250,y=450)
def all():
        root2=Tk()
        root2.config(bg='yellow')
        root2.title("LIBRARY MANAGEMANT SYSTEM")
        root2.state('zoomed')
        f1=Frame(root2,height=500,width=650,bg='black')
        f1.place(x=500,y=100)
        b1=Button(f1,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=rm).place(x=250,y=400)
        conn=sqlite3.connect('test.db')
        list3=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
        treess=create_tree(f1,list3)
        treess.place(x=25,y=50)
        c=conn.execute("select * from book_info")
        g=c.fetchall()
        if len(g)!=0:
            for row in g:
                treess.insert('',END,values=row)
        conn.commit()
        conn.close()



        
def student():
        root3 = Tk()
        root3.state('zoomed') 
        root3.config(bg='red')
        root3.title("LIBRARY MANAGEMANT SYSTEM")
        #root3.destroy()
        l1=Button(root3,text='Issue book',font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10,command=issue).place(x=12,y=100)
        l2=Button(root3,text='Return Book',font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10,command=returnn).place(x=12,y=200)
        l3=Button(root3,text='Student Activity',font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10,command=activity).place(x=12,y=300)
        l4=Button(root3,text='<< Main Menu',font='Papyrus 22 bold',fg='Orange',bg='Black',width=15,padx=10,command=mainmenu).place(x=12,y=600)

def issue():
        root3 = Tk()
        root3.state('zoomed') 
        root3.config(bg='red')
        root3.title("LIBRARY MANAGEMANT SYSTEM")
        idd=StringVar()
        studentt=StringVar()
        f1=Frame(root3,height=550,width=500,bg='black')
        f1.place(x=500,y=100)
        l1=Label(f1,text='Book ID : ',font='papyrus 15 bold',bg='black',fg='orange').place(x=50,y=100)
        e1=Entry(f1,width=25,bd=4,bg='orange',textvariable=issue).place(x=180,y=100)
        l2=Label(f1,text='Student Id : ',font='papyrus 15 bold',bg='black',fg='orange').place(x=50,y=150)
        e2=Entry(f1,width=25,bd=4,bg='orange',textvariable=issue).place(x=180,y=150)
        b1=Button(f1,text='Back',font='Papyrus 10 bold',fg='black',bg='orange',width=10,bd=3,command=rm).place(x=50,y=250)
        b1=Button(f1,text='Issue',font='Papyrus 10 bold',fg='black',bg='orange',width=10,bd=3,command=issue).place(x=200,y=250)
       
def returnn():
        root3 = Tk()
        root3.state('zoomed') 
        root3.config(bg='red')
        root3.title("LIBRARY MANAGEMANT SYSTEM")
        idd=StringVar()
        studentt=StringVar()
        f1=Frame(root3,height=550,width=500,bg='black')
        f1.place(x=500,y=100)
        l1=Label(f1,text='Book ID : ',font='papyrus 15 bold',fg='orange', bg='black').place(x=50,y=100)
        e1=Entry(f1,width=25,bd=4,bg='orange',textvariable=returnn).place(x=180,y=100)
        l2=Label(f1,text='Student Id : ',font='papyrus 15 bold',fg='orange', bg='black').place(x=50,y=150)
        e2=Entry(f1,width=25,bd=4,bg='orange',textvariable=returnn).place(x=180,y=150)
        b1=Button(f1,text='Back',font='Papyrus 10 bold',bg='orange',fg='black',width=10,bd=3,command=rm).place(x=50,y=250)
        b1=Button(f1,text='Return',font='Papyrus 10 bold',bg='orange',fg='black',width=10,bd=3,command=returnn).place(x=200,y=250)
        f1.grid_propagate(0)
        
def activity():
        root3 = Tk()
        root3.state('zoomed') 
        root3.config(bg='red')
        root3.title("LIBRARY MANAGEMANT SYSTEM")
        idd=StringVar()
        studentt=StringVar()
        f1=Frame(root3,height=550,width=500,bg='black')
        f1.place(x=500,y=80)
        list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        trees=create_tree(f1,list2)
        trees.place(x=50,y=150)
        l1=Label(f1,text='Book/Student ID : ',font='Papyrus 15 bold',fg='Orange',bg='black').place(x=50,y=30)
        e1=Entry(f1,width=20,bd=4,bg='orange',textvariable=activity).place(x=280,y=35)
        l2=Label(f1,text='Student Id : ',font='papyrus 15 bold',fg='orange',bg='black').place(x=50,y=80)
        e2=Entry(f1,width=20,bd=4,bg='orange',textvariable=activity).place(x=180,y=80)
        b1=Button(f1,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=rm).place(x=340,y=450)
        b1=Button(f1,text='Search',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=activity).place(x=40,y=450)
        b1=Button(f1,text='All',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=activity).place(x=190,y=450)
        f1.grid_propagate(0)
# ====================================== back button ========================================
def rm():
        f1.destroy()

# ====================================== menu button ========================================
def mainmenu():
        root.destroy()
        a=menu()

# ========================================= adddata ==========================================
def adddata():
        
        a=id.get()
        b=name.get()
        c=author.get()
        d=genre.get()
        e=copies.get()
        f=location.get()
        conn = mc.connect(host="localhost",user="root", password="", database="library")
        cur = conn.cursor()
        cur.execute("insert into addbook(BookID,TitleName,Author,Genre,Copies,Location) values('"+a+"', '"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')")
        
        try:
            if (a and b and c and d and e and f)=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                conn.execute("insert into addbook \values (?,?,?,?,?,?)",(a.capitalize(),b.capitalize(),c.capitalize(),d.capitalize(),e.capitalize(),f.capitalize()))
                conn.commit()
                messagebox.showinfo("Success","Book added successfully")
        except mysql.connectorError:
            messagebox.showinfo("Error","Book is already present.")

        conn.close()        

def create_tree(plc,lists):
        tree=ttk.Treeview(plc,height=13,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            tree.heading("#"+str(n+1),text=lists[n])
            tree.column(""+lists[n],width=100)
            n=n+1
        return tree

def serch1():
        k=sid.get()
        if k!="":
            list4=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
            trees=create_tree(f1,list4)
            trees.place(x=25,y=150)
            conn = mc.connect(host="localhost",user="root", password="", database="library")

            c=conn.execute("select * from book_info where ID=? OR TITLE=? OR AUTHOR=? OR GENRE=?",(k.capitalize(),k.capitalize(),k.capitalize(),k.capitalize(),))
            cur = conn.cursor()
            a=c.fetchall()
            if len(a)!=0:
                for row in a:

                    trees.insert("",END,values=row)
                conn.commit()
                conn.close()
                trees.bind('<<TreeviewSelect>>')
                variable = StringVar(f1)
                variable.set("Select Action:")


                cm =ttk.Combobox(f1,textvariable=variable ,state='readonly',font='Papyrus 15 bold',height=50,width=15,)
                cm.config(values =('Add Copies', 'Delete Copies', 'Delete Book'))

                cm.place(x=50,y=100)
                cm.pack_propagate(0)


                cm.bind("<<ComboboxSelected>>",combo)
                cm.selection_clear()
            else:
                messagebox.showinfo("Error","Data not found")



        else:
            messagebox.showinfo("Error","Search field cannot be empty.")

def combo(event):
        var_Selected = cm.current()
        l7=Label(f1,text='copies to update: ',font='Papyrus 10 bold',bd=1).place(x=250,y=700)
        if var_Selected==0:
            copies(var_Selected)
        elif var_Selected==1:
            copies(var_Selected)
        elif var_Selected==2:
            deleteitem()
def deleteitem():
        
        try:
            curItem = trees.focus()

            c1=trees.item(curItem,"values")[0]
            b1=Button(f1,text='Update',font='Papyrus 10 bold',width=9,bd=3,command=delete2).place(x=500,y=97)

        except:
            messagebox.showinfo("Empty","Please select something.")

def delete2():
        conn = mc.connect(host="localhost",user="root", password="", database="library")
        cur = conn.cursor()
        cd=conn.execute("select * from book_issued where BOOK_ID=?",(c1,))
        ab=cd.fetchall()
        if ab!=0:
            conn.execute("DELETE FROM book_info where ID=?",(c1,));
            conn.commit()
            messagebox.showinfo("Successful","Book Deleted sucessfully.")
            trees.delete(curItem)
        else:
            messagebox.showinfo("Error","Book is Issued.\nBook cannot be deleted.")
        conn.commit()
        conn.close()


def copies(varr):
        try:
            curItem = trees.focus()
            c1=trees.item(curItem,"values")[0]
            c2=trees.item(curItem,"values")[4]
            scop=IntVar()
            e5=Entry(f1,width=20,textvariable=scop)
            e5.place(x=310,y=100)
            if varr==0:
                b5=Button(f1,text='Update',font='Papyrus 10 bold',bg='orange',fg='black',width=9,bd=3,command=copiesadd).place(x=500,y=97)
            if varr==1:
                b6=Button(f1,text='Update',font='Papyrus 10 bold',bg='orange',fg='black',width=9,bd=3,command=copiesdelete).place(x=500,y=97)
        except:
            messagebox.showinfo("Empty","Please select something.")

def copiesadd():
        no=e5.get()
        if int(no)>=0:

            conn = mc.connect(host="localhost",user="root", password="", database="library")
            cur = conn.cursor()

            conn.execute("update book_info set COPIES=COPIES+? where ID=?",(no,c1,))
            conn.commit()

            messagebox.showinfo("Updated","Copies added sucessfully.")
            serch1()
            conn.close()

        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

def copiesdelete():
        no1=e5.get()
        if int(no1)>=0:
            if int(no1)<=int(c2):
                conn = mc.connect(host="localhost",user="root", password="", database="library")
                cur = conn.cursor()

                conn.execute("update book_info set COPIES=COPIES-? where ID=?",(no1,c1,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Updated","Deleted sucessfully")
                serch1()

            else:
                messagebox.showinfo("Maximum","No. of copies to delete exceed available copies.")
        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

def issuedbook():
        bookid=idd.get()
        studentid=studentt.get()
        conn = mc.connect(host="localhost",user="root", password="", database="library")
        cur = conn.cursor()
        cursor.execute("select ID,COPIES from book_info where ID=?",(bookid.capitalize(),))
        an=cursor.fetchall()
        if (bookid and studentid!=""):
            if an!=[]:
                for i in an:
                    if i[1]>0:
                        try:
                            conn.execute("insert into book_issued \
                            values (?,?,date('now'),date('now','+7 day'))",(bookid.capitalize(),studentid.capitalize(),))
                            conn.commit()
                            conn.execute("update book_info set COPIES=COPIES-1 where ID=?",(bookid.capitalize(),))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Updated","Book Issued sucessfully.")
                        except:
                            messagebox.showinfo("Error","Book is already issued by student.")

                    else:
                        messagebox.showinfo("Unavailable","Book unavailable.\nThere are 0 copies of the book.")
            else:
                messagebox.showinfo("Error","No such Book in Database.")
        else:
            messagebox.showinfo("Error","Fields cannot be blank.")
def returnbook():
        a=idd.get()
        b=studentt.get()

        conn = mc.connect(host="localhost",user="root", password="", database="library")
        cur = conn.cursor()

        fg=conn.execute("select ID from book_info where ID=?",(a.capitalize(),))
        fh=fg.fetchall()
        conn.commit()
        if fh!=None:
            c=conn.execute("select * from book_issued where BOOK_ID=? and STUDENT_ID=?",(a.capitalize(),b.capitalize(),))
            d=c.fetchall()
            conn.commit()
            if len(d)!=0:
                c.execute("DELETE FROM book_issued where BOOK_ID=? and STUDENT_ID=?",(a.capitalize(),b.capitalize(),));
                conn.commit()
                conn.execute("update book_info set COPIES=COPIES+1 where ID=?",(a.capitalize(),))
                conn.commit()

                messagebox.showinfo("Success","Book Returned sucessfully.")
            else:
                messagebox.showinfo("Error","Data not found.")
        else:
            messagebox.showinfo("Error","No such book.\nPlease add the book in database.")
        conn.commit()
        conn.close()
#def searchact(self):

def canvases(images):
        w =root.winfo_screenwidth()
        h =root.winfo_screenheight()
        photo=PhotoImage(file=images)
        photo=Image.open(images)
        photo1=photo.resize(w,h)
        photo2=ImageTk.PhotoImage(photo1)

        photo2 = ImageTk.PhotoImage(Image.open(images).resize(w, h))
        canvas = Canvas(root,width='%d'%w,height='%d'%h)
        canvas.grid(row = 0, column = 0)
        canvas.grid_propagate(0)
        canvas.create_image(0, 0, anchor = NW, image=photo2)
        canvas.image=photo2
        return canvas
def canvases(images,w,h):
    photo=Image.open(images)
    photo1=photo.resize(w,h)
    photo2=ImageTk.PhotoImage(photo1)

    photo2 = ImageTk.PhotoImage(Image.open(images).resize(w, h))
    canvas = Canvas(root, width='%d'%w, height='%d'%h)
    canvas.grid(row = 0, column = 0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor = NW, image=photo2)
    canvas.image=photo2
    return canvas
# ========================================= database connection ===================================================================
def putdataintomysql():
        username = i_username.get()
        password = i_password.get()
        conn = mc.connect(host="localhost",user="root", password="", database="library")
        cur = conn.cursor()
        cur.execute("insert into login(username,password) values('"+username+"', '"+password+"')")
        print('data transfered to mysql successfully ')
        conn.close()
    

# =========================================window creation===========================================================================
root = Tk() 
url = ImageTk.PhotoImage(Image.open(r"C:\Python310\Python Class\project\t3\finance.png")) # general syntax to open jpeg img
p1 = Label(root, image = url,height=1000,width=3000)
p1.pack(fill = "both")
root.state('zoomed')
root.title("LIBRARY MANAGEMANT SYSTEM")
mainframe = Frame(root)
mainframe.pack()
#=========================================== value assignment ===============================================================================
#login=putdataintomysql()
#login=putdataintomysql()
i_username=StringVar()
i_password=StringVar()


#=================================================== entry details ==================================================================

usrename = Entry(root,textvariable=i_username,font = ('Papyrus',15,'bold'),bg='black',fg='yellow').place(x=650, y=230)
password = Entry(root, textvariable=i_password,font = ('Papyrus',15,'bold'),bg='black',fg='yellow').place(x=650, y=330)

# =====================================================label details ================================================================
t=Label(root,text = "ADMIN LOGIN",font = ('Papyrus',30,'bold'),bg = 'black',fg = 'orange').place(x=500,y=100)

t=Label(root, text='UserName',font = ('Papyrus',15,'bold'),bg='black',fg='yellow').place(x=500, y=230)

t=Label(root, text='Password',font=('Papyrus',15,'bold'),bg='black',fg='yellow').place(x=500, y=330)

# ===========================================button inclusion in window frame ========================================================
t=Button(root, text="LOGIN",command= createnewwindow,font=('Papyrus', 15, 'bold'),width=25, bg='black',fg='yellow',).place(x=500, y=400)

root.mainloop()


