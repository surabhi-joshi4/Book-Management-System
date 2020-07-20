from tkinter import *
import mysql.connector as my
from tkinter.messagebox import *


win=Tk()
win.geometry("1200x1200+20+20")
win.title("Book management System")
win.config(bg="papaya whip")

lblnm=Label(text="Welcome to Admin Panel",font=("arial black",15),fg="lime green",bg="papaya whip")
lblnm.grid(row=0,column=1)
lblbid=Label(text="Enter Book id ",font=("arial black",10),fg="navy",bg="papaya whip")
lblbid.grid(row=3,column=0)
lblbname=Label(text="Enter Book name ",font=("arial black",10),fg="navy",bg="papaya whip")
lblbname.grid(row=4,column=0)
lblbprice=Label(text="Enter Book price ",font=("arial black",10),fg="navy",bg="papaya whip")
lblbprice.grid(row=5,column=0)
lblauthor=Label(text="Enter Author name ",font=("arial black",10),fg="navy",bg="papaya whip")
lblauthor.grid(row=6,column=0)
lblpublish=Label(text="Enter Publish year ",font=("arial black",10),fg="navy",bg="papaya whip")
lblpublish.grid(row=7,column=0)
lblbk=Label(text="Book list",font=("arial black",15),fg="lime green",bg="papaya whip")
lblbk.grid(row=16,column=4)
lblsearch=Label(text="Search book id",font=("arial black",10),fg="navy",bg="papaya whip")
lblsearch.grid(row=15,column=0)


txtbid=Entry(win,font=("arial black",10),fg="tomato")
txtbid.grid(row=3,column=1)
txtbname=Entry(win,font=("arial black",10),fg="tomato")
txtbname.grid(row=4,column=1)
txtbprice=Entry(win,font=("arial black",10),fg="tomato")
txtbprice.grid(row=5,column=1)
txtauthor=Entry(win,font=("arial black",10),fg="tomato")
txtauthor.grid(row=6,column=1)
txtpublish=Entry(win,font=("arial black",10),fg="tomato")
txtpublish.grid(row=7,column=1)
txtserach=Entry(win,font=("arial black",10),fg="tomato")
txtserach.grid(row=15,column=1)



from tkinter.ttk import *


frame=Frame(win)
frame.grid(row=20,column=4)

tree=Treeview(frame,columns=(1,2,3,4,5),height=5,show="headings")
tree.grid(row=20,column=4)


tree.heading(1,text="ID")
tree.heading(2,text="Name")
tree.heading(3,text="Price")
tree.heading(4,text="Author")
tree.heading(5,text="Publish Year")

tree.column(1,width=120)
tree.column(2,width=120)
tree.column(3,width=120)
tree.column(4,width=120)
tree.column(5,width=120)



db=my.connect(host='localhost',user='root',passwd='',database='bookmgmt',port='3306')
cur=db.cursor()

def saverec():
	try:
		bid=txtbid.get()
		bookname=txtbname.get()
		bookprice=txtbprice.get()
		bookauthor=txtauthor.get()
		bookpublishyear=txtpublish.get()
		sql="insert into book(bid,bookname,bookprice,bookauthor,bookpublishyear)values({},'{}',{},'{}',{})".format(bid,bookname,bookprice,bookauthor,bookpublishyear)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("Save","Book is added")
			sql="select * from book ORDER BY bid ASC"
			cur.execute(sql)
			data=cur.fetchall()
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))
				db.commit()
		else:
			showinfo("Try again")
			db.rollback()
	except Exception as e:
		print(e)	



def editrec():
	try:
		bid=txtbid.get()
		bookprice=txtbprice.get()
		sql="update book set bookprice={} where bid={}".format(bookprice,bid)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("Update","Book is updated")
			sql="select * from book ORDER BY bid ASC"
			cur.execute(sql)
			data=cur.fetchall()
			for i in tree.get_children():
				tree.delete(i)
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))
				db.commit()			
		else:
			showinfo("Try again")
			db.rollback()
	except Exception as e:
		print(e)
def delrec():
	try:
		bid=txtbid.get()
		sql="delete from book where bid={}".format(bid)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("Delete","Book is deleted")
			sql="select * from book ORDER BY bid ASC"
			cur.execute(sql)
			data=cur.fetchall()
			for i in tree.get_children():
				tree.delete(i)
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))	
				db.commit()
		else:
			showinfo("Try again")
			db.rollback()     
	except Exception as e:
		print(e)
def showrec():
	try:
		sql="select * from book ORDER BY bid ASC"
		cur.execute(sql)
		data=cur.fetchall()
		for i in tree.get_children():
			tree.delete(i)
		for val in data:
			tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))	
			db.commit() 
	except Exception as e:
		print(e)

def searchrec():
	try:
		bid=txtserach.get()
		sql="select * from book where bid={}".format(bid)
		cur.execute(sql)
		if cur.rowcount:
			showinfo("search","Id is search")
			data=cur.fetchall()
			for i in tree.get_children():
				tree.delete(i)
			for val in data:
				tree.insert('','end',values=(val[0],val[1],val[2],val[3],val[4]))	
				db.commit()
		else:
			showinfo("Try again")
			db.rollback()     
	except Exception as e:
		print(e)
def clearrec():
    txtbid.delete(first=0,last=22)
    txtbname.delete(first=0,last=22)
    txtbprice.delete(first=0,last=22)
    txtauthor.delete(first=0,last=22)
    txtpublish.delete(first=0,last=22)
    txtserach.delete(first=0,last=22)
  

save=Button(win,text="Add",width=12,command=saverec)
save.grid(row=11,column=0)
edit=Button(win,text="Update",width=12,command=editrec)
edit.grid(row=11,column=1)
delete=Button(win,text="Delete",width=12,command=delrec)
delete.grid(row=12,column=0)
clear=Button(win,text="Clear",width=12,command=clearrec)
clear.grid(row=12,column=1)
search=Button(win,text="Search",width=12,command=searchrec)
search.grid(row=15,column=2)
show=Button(win,text="Show all books",width=15,command=showrec)
show.grid(row=14,column=0)


win.mainloop()    						
db.close()
