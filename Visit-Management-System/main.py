from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkcalendar import  *
from tktimepicker import AnalogPicker, AnalogThemes
from sqlite3 import *
from getpass import *
from pyrebase import *

firebaseConfig = {
	"databaseURL" :"https://stud-c8d05-default-rtdb.firebaseio.com/",
	"apiKey": "AIzaSyCTNfC5Rpmrhu4a7XJrItnR-T2_Vmsx1Oo",
	"authDomain": "stud-c8d05.firebaseapp.com",
	"projectId": "stud-c8d05",
	"storageBucket": "stud-c8d05.appspot.com",
	"messagingSenderId": "9301916004",
	"appId": "1:9301916004:web:7b5aa9ec94d6bc6e12e271",
	"measurementId": "G-84XSTD786N"
	};

fb = initialize_app(firebaseConfig)
db = fb.database()

screen = Tk()
screen.title("Visitor manangement system")
screen.geometry("800x600+50+50")
screen.iconbitmap("visit.ico")
t = ("Century" , 30 , "bold" , "italic")
f =("Century" , 20 , "bold" , "italic")

def login(): 
	username = "varsha" 
	password = "12345"

	if entUser.get() == username and entPass.get() == password:
		showinfo("Login Successful","You have logged in Successfully")
		root.deiconify()
		screen.withdraw()

	elif entUser.get() == username and entPass.get() != password: 	
		showerror('Wrong password','Please check your password')
		entPass.delete(0 , END)
		entPass.focus() 
        
	elif entUser.get() != username and entPass.get() == password: 	
		showerror('Wrong username','Please check your username') 
		entUser.delete(0 , END)
		entUser.focus()
        
	else: 
		showerror("Login Failed","Invalid Username and password")
		entUser.delete(0 , END)
		entPass.delete(0 , END)
		entUser.focus()

labtitle1 =Label(screen , text = " Visitor Management System" , font = t)
labtitle1.place(x = 100 , y = 50)

lablogin =Label(screen , text = " Login Page " , font = f)
lablogin.place(x = 330 , y = 150)

labUser =Label(screen , text = " Enter Username " , font = f)
labUser.place(x = 300 , y = 220)

entUser = Entry(screen , font = f)
entUser.place(x = 250, y = 270)

labPass =Label(screen , text = " Enter Password " , font = f)
labPass.place(x = 300 , y = 370)

entPass = Entry(screen  , font = f , show = "*")
entPass.place(x = 250, y = 420)

btnLogin = Button(screen , text = "Login" , font = f , command = login)
btnLogin.place(x= 350, y =500 )




root =  Toplevel(screen)
root.title("Visitor manangement system")
root.geometry("800x600+50+50")
root.iconbitmap("visit.ico")
t = ("Century" , 30 , "bold" , "italic")
f = ("Arial" , 15 , "bold" )
m= (1)

labtitle =Label(root , text = " Visitor Management System" , font = t)
labtitle.place(x = 100 , y = 50)

def show():
	name = entName.get()
	phone = entPhn.get()
	visitee = entVisitee.get()
	date = entDate.get()
	time = entTime.get()
	office = clicked.get()

	if not entName.get():
		showerror("Issue" , "You did not enter name")		
		entName.focus()
		return

	while True:
		if name != '' and all(chr.isalpha() or chr.isspace() for chr in name):
			break
		else:
			showerror("Issue" , " Name is contain only alphabets")
			entName.delete(0 , END)
			entName.focus()
			return

	if name.isdigit():
		showerror("Issue" , "Name is not contain numbers")
		entName.delete(0 , END)
		entName.focus()
		return

	if name.isspace():
		showerror("Issue" , "Name is not contain space")
		entName.delete(0 , END)
		entName.focus()
		return

	if not entPhn.get():
		showerror("Issue" , "You did not enter phone no")
		entPhn.focus()
		return

	if not phone.isdigit():
		showerror("Issue" , "Phone is not contain alphabets")
		entPhn.delete(0 , END)
		entPhn.focus()
		return

	if (len(entPhn.get()) != 10):
		showerror("Issue" , "Phone no is contain 10 digit")
		entPhn.delete(0 , END)
		entPhn.focus()
		return

	if not entVisitee.get():
		showerror("Issue" , "You did not enter visitee name")
		entVisitee.focus()
		return

	if visitee.isdigit():
		showerror("Issue" , "Name is not contain numbers")
		entVisitee.delete(0 , END)
		entVisitee.focus()
		return

	if visitee.isspace():
		showerror("Issue" , "Name is not contain space")
		entVisitee.delete(0 , END)
		entVisitee.focus()
		return

	while True:
		if visitee != '' and all(chr.isalpha() or chr.isspace() for chr in visitee):
			break
		else:
			showerror("Issue" , " Name is contain only alphabets")
			entVisitee.delete(0 , END)
			entVisitee.focus()
			return

	if not entDate.get():
		showerror("Issue" , "You did not enter date")
		entDate.focus()
		return

	if not entTime.get():
		showerror("Issue" , "You did not enter time")
		entTime.focus()
		return


	phone = int(entPhn.get())
	con = None
	try :
		con = connect("visit.db")
		cursor = con.cursor()
		sql = "insert into visit values('%s','%d','%s','%s','%s','%s')"
		cursor.execute(sql % (name , phone , visitee , date ,time , office))
		con.commit()
		showinfo("Done","added")
		entName.delete(0 , END)
		entPhn.delete(0 , END)
		entVisitee.delete(0 , END)
		entDate.delete(0 , END)
		entTime.delete(0 , END)
		entName.focus()
	except Exception as e:
		msg= "issue" + str(e)
		showerror("issue" ,msg)

	finally :
		if con is not None:
			con.close()
	info = { "name":name , "phone" : phone , "visitee" : visitee , "date" : date , "time" : time , "office" :office }
	db.child("fb").push(info)


labName =Label(root , text = "Enter Name" , font = f)
labName.place(x = 50 , y = 150)

entName = Entry(root , font = f ,width = 20)
entName.place(x = 300 , y = 150)

labPhn =Label(root , text = " Enter phone Number " , font = f)
labPhn.place(x = 50 , y = 200)

entPhn = Entry(root , font = f ,width = 20)
entPhn.place(x = 300 , y = 200)

labVisitee =Label(root , text = "Enter Visitee " , font = f)
labVisitee.place(x = 50 , y = 250)

entVisitee = Entry(root , font = f ,width = 20)
entVisitee.place(x = 300 , y = 250)



def pick_date(event):
	global cal , date_window

	date_window = Toplevel()
	date_window.grab_set()
	date_window.title('select date')
	date_window.geometry('250x250+590+370')
	cal = Calendar(date_window , selectmode="day" , date_pattern = "mm/dd/yyyy")
	cal.place(x= 0 , y = 0)

	submit_btn = Button(date_window , text = "submit" , font = f , command = grab_date)
	submit_btn.place(x=80 , y = 190)

def grab_date():
	entDate.delete(0 , END)
	entDate.insert(0 , cal.get_date())	
	date_window.destroy()

labDate =Label(root , text = "Select Date " , font = f)
labDate.place(x = 50 , y = 300)

entDate = Entry(root , font = f ,width = 20)
entDate.place(x = 300 , y = 300)
entDate.bind("<1>" , pick_date)


def pick_time(event):
	global clock , time_window

	time_window = Toplevel()
	time_window.grab_set()
	time_window.title('select time')
	time_window.geometry('300x300+590+370')
	clock = AnalogPicker(time_window)
	clock.pack(expand=True, fill="both")

	theme = AnalogThemes(clock)
	theme.setDracula()

	submit_btn = Button(time_window , text = "submit" , font = m , command = grab_time)
	submit_btn.place(x=10 , y = 250 , width = 60 )

def grab_time():
	entTime.delete(0 , END)
	entTime.insert(0 , clock.time())	
	time_window.destroy()

labTime =Label(root , text = " Select Time " , font = f)
labTime.place(x = 50 , y = 350)

entTime = Entry(root , font = f ,width = 20)
entTime.place(x = 300 , y = 350)
entTime.bind("<1>" , pick_time)


options = [ "Office 1" , "Office 2" , "Office 3" , "Office 4" , "Office 5"]

clicked = StringVar()
clicked.set("Office1")
drop = OptionMenu(root , clicked , *options )
drop.place(x = 300 , y = 400, width = 180)

labOffice =Label(root , text = " Select office " , font = f)
labOffice.place(x = 50 , y = 400)


btn = Button(root , text = "Submit" , font = f , command = show)
btn.place(x= 350, y =500)


def View():
	view.deiconify()
	root.withdraw()
	vs_data.delete(1.0 , END)
	con = None
	try : 
		con = connect("visit.db")
		cursor = con.cursor()
		sql = "select * from visit"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = " "
		for d in data :
			info = info + "Name : " + str(d[0]) + "\t"+ "Phone No. : " + str(d[1]) + "\t"+ "Visitee : " + str(d[2])  + "\t" + "Date : " + str(d[3]) + "\t"+ "Time : " + str(d[4]) + "\t"+ "Office : " + str(d[5])  + "\n"
		vs_data.insert(INSERT , info)
	except Exception as e:
		showerror("issue" , e)
	finally:
		if con is not None:
			con.close()

btnView = Button(root , text = "View Data" , font = f , command = View )
btnView.place(x= 150, y =500 )


def deleted():
	deleted.deiconify()
	root.withdraw()

btnDel = Button(root , text = "delete record" , font = f , command = deleted )
btnDel.place(x= 500, y =500 )

root.withdraw()


def back():
	root.deiconify()
	view.withdraw()


view = Toplevel(root)
view.title("View Data")
view.geometry("1300x600+50+50")
view.iconbitmap("visit.ico")
d = ("Arial" , 15 , "bold")

vs_data = ScrolledText(view , width = 110 , height = 15 , font = d )
vs_data.place(x= 50, y =50 )

vs_back = Button(view , text = "Add More", font = f , command = back )
vs_back.place(x= 550, y =450 )

view.withdraw()




def delete():
	con = None 
	try:
		con = connect("visit.db")
		cursor = con.cursor()
		sql = "delete from visit where name = '%s' and phone = '%d'"
		name = entDel_N.get()
		phone = int(entDel_phn.get())
		cursor.execute(sql % (name , phone ))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("done","record deleted")
			entDel_N.delete(0 , END)
			entDel_phn.delete(0 , END)
			entDel_N.focus()
		else :
			showinfo("issue" , "record does not exists")
			entDel_N.delete(0 , END)
			entDel_phn.delete(0 , END)
			entDel_N.focus()
	except Exception as e:
		showerror("issue" , str(e))
		entDel_N.delete(0 , END)
		entDel_phn.delete(0 , END)
		entDel_N.focus()
	finally:
		if con is not None:
			con.close()

deleted = Toplevel(root)
deleted.title("Delete Data")
deleted.geometry("800x400+50+50")
deleted.iconbitmap("visit.ico")

labDel_N =Label(deleted , text = " enter name " , font = f)
labDel_N.place(x = 50 , y = 50)

entDel_N = Entry(deleted , font = f ,width = 20)
entDel_N.place(x = 300 , y = 50)

labDel_Phn =Label(deleted , text = " enter phone no. " , font = f)
labDel_Phn.place(x = 50 , y = 150)

entDel_phn = Entry(deleted , font = f ,width = 20)
entDel_phn.place(x = 300 , y = 150)

btnDelete = Button(deleted , text = "Delete" , font = f , command = delete )
btnDelete.place(x= 300, y =250 )

def delBack():
	root.deiconify()
	deleted.withdraw()

btnDel_B = Button(deleted , text = "Add more" , font = f , command = delBack )
btnDel_B.place(x= 100, y =250 )

def View1():
	view.deiconify()
	deleted.withdraw()
	vs_data.delete(1.0 , END)
	con = None
	try :
		con = connect("visit.db")
		cursor = con.cursor()
		sql = "select * from visit"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = " "
		for d in data :
			info = info + "Name : " + str(d[0]) + "\t"+ "Phone No. : " + str(d[1]) + "\t"+ "Visitee : " + str(d[2])  + "\t" + "Date : " + str(d[3]) + "\t"+ "Time : " + str(d[4]) + "\t"+ "Office : " + str(d[5])  + "\n"
		vs_data.insert(INSERT , info)
	except Exception as e:
		showerror("issue" , e)
	finally:
		if con is not None:
			con.close()
btnView = Button(deleted , text = "View Data" , font = f , command = View1 )
btnView.place(x= 500, y =250 )


deleted.withdraw()


def confirmExit():
	if askyesno('Exit' , 'Do you want to exit?'):
		root.destroy()
root.protocol('WM_DELETE_WINDOW' , confirmExit)

screen.mainloop()







