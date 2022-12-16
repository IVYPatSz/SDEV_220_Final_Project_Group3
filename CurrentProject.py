#Final project sketch
#address book

#This is just more simple it import everything
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import askyesno, askquestion

######## CREATE A WINDOW ########
root = Tk() #root can be anything but for simplicity is called root
root.geometry('500x400')#width x height we do not need it to be so big
root.title("Address Book")#title of the window
root.resizable(False,False)#non-resizeble window--> https://www.tutorialspoint.com/how-to-make-a-tkinter-window-not-resizable

######## USING TTK TO CUSTOM BUTTONS ########
#more info here -->https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-style-layer.html
style = Style()

#the style of text inside the button
style.configure('TButton', font = ('Arial', 15, 'bold'), borderwidth = '2')

#This will change the color of the button to blue when the mouse is over it
#foreground is the text color inside the button
#background is the color that affects the whole button
style.map('TButton', foreground = [('active', '!disabled', 'blue')], background = [('active', 'yellow')])

#####CREATES A PLACE WHERE WE CAN SEE THE CONTACTS######
#I took my time to research around and I added a little bit to a code we
#already had so that the table shows in the right at all time more info here -->https://www.tutorialspoint.com/python/tk_pack.htm
#I added this part - jj
frame = Frame(root)
frame.place(x=320, y=25)
#THIS IS Patrick's part of the code 
scroll_bar = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll_bar.set, height=12)
select = Listbox(frame, xscrollcommand=scroll_bar.set, width=17)
scroll_bar.config (command=select.yview)
#I added this part - jj
scroll_bar.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

######## CREATE STRINGS TO STORE USER INFO ########
# StringVar() holds a string data where we can set text value and can retrieve it
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

######## UPTADE ########  - Samuel [working]
def update_book() :
    select.delete(0,END)
    for f,l,p,e,c,s,c,p,s in contact_list : #I know why Samuel put f,l,p,e,c,s,c,p,s  LOL
        select.insert (END, '-->'+f+' '+l )
update_book()

######## SELECT ########

#Samuel had a code on the remove def that relied on selection a short function was needed
#to be honest this can be of help with every other function
def Selected():
    return int(select.curselection()[0])
    
######## ADD FUNCTION ######## - Jordy [working]
class ADD:
    def AContact():
        contact_list.append([fname.get(),lname.get(),number.get(), email.get(), country.get(), state.get(), city.get(), postCode.get(), street.get()])
        print(*contact_list)
        update_book()
    Button(root,text="ADD", command = AContact).place(x= 10, y=220)

######## EDIT FUNCTION ######## -Samuel [COMPLETE]
class ED:    
    def EDIT():
        contact_list[Selected()] = [fname.get(),lname.get(), number.get(), email.get(), country.get(), state.get(), city.get(), postCode.get(), street.get()]
        update_book()
    Button(root,text="EDIT",  command=EDIT).place(x= 150, y=220)

######## REMOVE FUCTION ######## - Samuel [working]
class DELETE:
    def REMOVE():
        del contact_list[Selected()]#the int part and the curselection was changed to a function on top
        update_book()
    Button(root,text="REMOVE", command = REMOVE).place(x=10, y=260)

######## RESET FUNCTION ######## - Samuel [working]
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
   
######## SHOW FUNCTION ######## -Jordy [testing]
#now it will show every pieace of information in the entry boxes not on the big box on the right
class SHOW:
    def Show_conct():
        FNAME,LNAME,NUMBER,EMAIL,COUNTRY,STATE,CITY,POSTCODE,STREET = contact_list[Selected()]#
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
        answer = askyesno(title='Confirm',
            message='You are about to quit, are you sure?')
        if answer:
            root.destroy()

    Button(root, text="END", command = sure).place(x=150, y=300)

######## DEFINE TEXT AND ENTRY BOXES ########
Label(root, text = 'First Name:', font='Arial').place(x= 20, y=20)
Entry(root, textvariable = fname).place(x= 120, y=20)

Label(root, text = 'Last Name:', font='Arial').place(x= 20, y=40)
Entry(root, textvariable = lname).place(x= 120, y=40)

Label(root, text = 'Number:', font='Arial').place(x= 20, y=60)
Entry(root, textvariable = number).place(x= 120, y=60)

Label(root, text = 'Email:', font='Arial').place(x= 20, y=80)
Entry(root, textvariable = email).place(x= 120, y=80)

Label(root, text = 'Country:', font='Arial').place(x= 20, y=100)
Entry(root, textvariable = country).place(x= 120, y=100)

Label(root, text = 'State:', font='Arial').place(x= 20, y=120)
Entry(root, textvariable = state).place(x= 120, y=120)

Label(root, text = 'City:', font='Arial').place(x= 20, y=140)
Entry(root, textvariable = city).place(x= 120, y=140)

Label(root, text = 'Post Code:', font='Arial').place(x= 20, y=160)
Entry(root, textvariable = postCode).place(x= 120, y=160)

Label(root, text = 'Street:', font='Arial').place(x= 20, y=180)
Entry(root, textvariable = street).place(x= 120, y=180)

######## SHOWS THE GUI ########
root.mainloop()