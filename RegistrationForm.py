from tkinter import*
import re
import sqlite3
import tkinter.messagebox
root=Tk()
root.resizable(width=False,height=False)
frame1=Frame(width=500,height=700)
frame1.pack()

FirstName=StringVar()
SecondName=StringVar()
CollegeName=StringVar()
Emailid=StringVar()
Contact=StringVar()

def database():
	fname=FirstName.get()
	sname=SecondName.get()
	college=CollegeName.get()
	email=Emailid.get()
	contact=Contact.get()
	course=s.get()
	conn=sqlite3.connect("StudentRecord.db")
	with conn:
		cursor=conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS Student(FirstName char(20),SecondName char(20),CollegeName char(30),Emailid char(60),Contact int,Course char(20))')
		cursor.execute('INSERT INTO Student (FirstName,SecondName,CollegeName,Emailid,Contact,Course) VALUES(?,?,?,?,?,?)',(fname,sname,college,email,contact,course))
		conn.commit()
		cursor.close()
		
#########validation#########

def isValidEmail(Emailid):
	 if(len(e5.get()) > 7):
	 	if(re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", Emailid) != None):
	 		return True
	 	else:
	 		return False
	 
 
def val():
	a=e2.get()
	b=e3.get()
	c=e4.get()
	e=e6.get()
	f=s.get()
	if(len(a)>0 and len(b)>0 and len(c)>0   and isValidEmail(Emailid.get()) and e.isdigit() and (len(e) == 10) and len(f)>0):
		button.config(state="normal")
		return True
	else:
		return False
		
############################	    
def msg():
	if(val()):
		database()
		FirstName.set("")
		SecondName.set("")
		CollegeName.set("")
		Emailid.set("")
		Contact.set("")
		s.set("")
		tkinter.messagebox.showinfo("info","your response have been submitted : )")
	else:
		tkinter.messagebox.showwarning("warning",": ( make sure you filled every field and your phone number and email are correct")
	return
	

##########Entry and labels########

frame=Frame(root,bg="#ffcc99")
frame.place(relwidth=1,relheight=1)


l1=Label(root,text="Registration Form",width=20,font=("calibri",15,"underline"),bg="sky blue",fg="white")
l1.place(x=150,y=50)

l2=Label(root,text="First Name",bg="gray",fg="white")
l2.place(x=70,y=130)
e2=Entry(root,text=FirstName,highlightbackground="#404040",highlightcolor="#ff0000")
e2.place(x=70,y=160)

l3=Label(root,text="Second Name",bg="gray",fg="white")
l3.place(x=70,y=210)
e3=Entry(root,text=SecondName,highlightbackground="#404040",highlightcolor="#ff0000")
e3.place(x=70,y=240)

l4=Label(root,text="College Name",bg="gray",fg="white")
l4.place(x=70,y=290)
e4=Entry(root,text=CollegeName,highlightbackground="#404040",highlightcolor="#ff0000")
e4.place(x=70,y=320)

l5=Label(root,text="Email id",bg="gray",fg="white")
l5.place(x=70,y=370)
e5=Entry(root,text=Emailid,highlightbackground="#404040",highlightcolor="#ff0000")
e5.place(x=70,y=400)

l6=Label(root,text="Contact ",bg="gray",fg="white")
l6.place(x=70,y=450)
e6=Entry(root,text=Contact,highlightbackground="#404040",highlightcolor="#ff0000")
e6.place(x=70,y=480)

l7=Label(root,text="Course",bg="gray",fg="white")
l7.place(x=70,y=530)

########Button and dropdown######

list7={'c','c++','java','python','android'}
s=StringVar()

backlabel=Label(root,width=20,height=2,bg="#404040").place(x=65,y=557)


droplist=OptionMenu(root,s,*list7)
droplist.config(width=15,bg='white')
s.set("")
droplist.place(x=70,y=560)

optionlabel=Label(root,text="-: select",bg="gray",fg="white")
optionlabel.place(x=220,y=565)


button=Button(root,text="Submit",bg="red",fg="white",command=msg)
button.place(x=150,y=630,relwidth=0.4,relheight=0.04)

root.bind(val)

#############################
root.mainloop()
