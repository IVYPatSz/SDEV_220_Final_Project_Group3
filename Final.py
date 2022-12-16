#Final project
#Team Leader: Patrick Szpak
#Team: Samuel Gest, and Jordy Jordan
#Address Book
#This program will store user information and then the user could either delete, edit, add, show, and reset.


#import everything
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import askyesno, askquestion

######## CREATE A WINDOW ########
root = Tk()
root.geometry('500x400')
root.title("Address Book")
root.resizable(False,False)

######## USING TTK TO CUSTOM BUTTONS ########
style = Style()
style.configure('TButton', font = ('Arial', 15, 'bold'), borderwidth = '2')
style.map('TButton', foreground = [('active', '!disabled', 'blue')], background = [('active', 'RED')])

######## CREATES A PLACE WHERE WE CAN SEE THE CONTACTS ########
frame = Frame(root)
frame.place(x=300, y=20)
scroll_bar = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

######## CREATE STRINGS TO STORE USER INFO ########
fname = StringVar()
lname = StringVar()
number = StringVar()
email = StringVar()
country = StringVar()
state = StringVar()
city = StringVar()
postCode = StringVar()
street = StringVar()

######## CREATE A LIST OF CONTACTS ########
contact_list = [
    ['Patrick','Szpak', '6802345555','overthere@gmail.com','United States', 'California', 'Cameron Park', '956882','3400 Cameron Park Dr'],
    ['Samuel','Gest','545645562','there@gmail.com','United States','Oregon','Portland','97210','2222 NW Raleigh St'],
    ['Jordy','Jordan', '0176738493', 'here@gmail.com', 'United States', 'Michigan','Albion','49224','119 N Superior St' ],
    ]

######## UPTADE ######## 
def update_book() :
    contact_list.sort()
    select.delete(0,END)
    for f,l,p,e,c,s,c,p,s in contact_list :
        select.insert (END, '-->'+f+' '+l )
update_book()

######## SELECT ########
def Selected():
    return int(select.curselection()[0])

######## ADD FUCTION ########
class ADD:
    def AContact():
        contact_list.append([fname.get(),lname.get(),number.get(), email.get(), country.get(), state.get(), city.get(), postCode.get(), street.get()])
        print(*contact_list)
        update_book()
    Button(root,text="ADD", command = AContact).place(x= 10, y=220)

######## EDIT FUNCTION ######## 
class ED:    
    def EDIT():
        contact_list[Selected()] = [fname.get(),lname.get(), number.get(), email.get(), country.get(), state.get(), city.get(), postCode.get(), street.get()]
        update_book()
    Button(root,text="EDIT",  command=EDIT).place(x= 150, y=220)

######## REMOVE FUCTION ########
class DELETE:
    def REMOVE():
        del contact_list[Selected()]#the int part and the curselection was changed to a function on top
        update_book()
    Button(root,text="REMOVE", command = REMOVE).place(x=10, y=260)
    
######## RESET FUNCTION ########
class RE:
    def RESET():
        fname.set('')
        lname.set('')
        number.set('')
        email.set('')
        country.set('')
        state.set('')
        city.set('')
        postCode.set('')
        street.set('')
    Button(root, text="RESET", command = RESET).place(x=10, y=300)

######## SHOW FUNCTION ######## 
class SHOW:
    def Show_conct():
        FNAME,LNAME,NUMBER,EMAIL,COUNTRY,STATE,CITY,POSTCODE,STREET = contact_list[Selected()]
        fname.set(FNAME)
        lname.set(LNAME)
        number.set(NUMBER)
        email.set(EMAIL)
        country.set(COUNTRY)
        state.set(STATE)
        city.set(CITY)
        postCode.set(POSTCODE)
        street.set(STREET)
    Button(root,text="VIEW",  command = Show_conct).place(x= 150, y=260)

######## EXIT ########
class FIN:
    
    def sure():
        ans = askyesno(title='Confirm',
            message='You are about to quit, are you sure?')
        if ans:
            root.destroy()

    Button(root, text="END", command = sure).place(x=150, y=300)

######## DEFINE TEXT AND ENTRY BOXES ########
Label(root, text = 'First Name', font='Arial').place(x= 30, y=20)
Entry(root, textvariable = fname).place(x= 150, y=20)

Label(root, text = 'Last Name', font='Arial').place(x= 30, y=40)
Entry(root, textvariable = lname).place(x= 150, y=40)

Label(root, text = 'Number', font='Arial').place(x= 30, y=60)
Entry(root, textvariable = number).place(x= 150, y=60)

Label(root, text = 'Email', font='Arial').place(x= 30, y=80)
Entry(root, textvariable = email).place(x= 150, y=80)

Label(root, text = 'Country', font='Arial').place(x= 30, y=100)
Entry(root, textvariable = country).place(x= 150, y=100)

Label(root, text = 'State', font='Arial').place(x= 30, y=120)
Entry(root, textvariable = state).place(x= 150, y=120)

Label(root, text = 'City', font='Arial').place(x= 30, y=140)
Entry(root, textvariable = city).place(x= 150, y=140)

Label(root, text = 'Post Code', font='Arial').place(x= 30, y=160)
Entry(root, textvariable = postCode).place(x= 150, y=160)

Label(root, text = 'Street', font='Arial').place(x= 30, y=180)
Entry(root, textvariable = street).place(x= 150, y=180)

######## SHOWS THE GUI ########
root.mainloop()