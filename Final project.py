#Final project sketch
#address boo
from tkinter import *
import tkinter as tk


########create a window########
root = tk.Tk()
root.geometry("1080x800")#width x height
root.title("Address Book")#title of the window
label = tk.Label(root, text="Hello there!", font=('Arial', 18))



#####Create a List of Contacts#####
contact_list = [] #

# StringVar() holds a string data where we can set text value and can retrieve it
fname = StringVar()
lname = StringVar()
number = StringVar()
email = StringVar()
country = StringVar()
state = StringVar()
city = StringVar()
Postcode = StringVar()
street = StringVar()




########FUNCTIONS########



########inputs########
#note: a grip is a 2-dimensional table
#Text for the inputs
tk.Label(root, text="First Name").grid(row=0)
tk.Label(root, text="Last Name").grid(row=1)
tk.Label(root, text="Number").grid(row=2)
tk.Label(root, text="Email").grid(row=3)
tk.Label(root, text="Country").grid(row=4)
tk.Label(root, text="State").grid(row=5)
tk.Label(root, text="City").grid(row=6)
tk.Label(root, text="postCode").grid(row=7)
tk.Label(root, text="Street").grid(row=8)


#User input/entry after the text
Fname = tk.Entry(root)
Lname = tk.Entry(root)
Number = tk.Entry(root)
Email = tk.Entry(root)
Country = tk.Entry(root)
State = tk.Entry(root)
City = tk.Entry(root)
postCode = tk.Entry(root)
Street = tk.Entry(root)

#how it will show the text
Fname.grid(row=0, column=1)
Lname.grid(row=1, column=1)
Number.grid(row=2, column=1)
Email.grid(row=3, column=1)
Country.grid(row=4, column=1)
State.grid(row=5, column=1)
City.grid(row=6, column=1)
postCode.grid(row=7, column=1)
Street.grid(row=8, column=1)



########add contacts########
def AddContact():
    contact_list.append([Fname.get(), Lname.get(), Number.get(), Email.get(), Country.get(), State.get(), City.get(), postCode.get(), Street.get()])
    print(*contact_list)


########remove########
def remove():
    del contact_list[int(select.curselection()[0])]
    update_book()


########edit########


########show########



######UPDATE ADDRESS BOOK######
def update_book():
    select.delete(0,END)
    for n,p,a in contact_list:
        select.insert(END, n)

# def Show_List():
#     print("First Name: %s\nLast Name: %s \nNumber: %s \nEmail: %s \nCountry: %s \nState: %s \nCity: %s \npostCode: %s \nStreet: %s" % (Fname.get(), Lname.get(), Number.get(), Email.get(), Country.get(), State.get(), City.get(), postCode.get(), Street.get())  
#     )
#AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH WHYYYYYYYYY
def something():
    text1=Text(root, width=20, height=15)
    text1.place(x=300, y=0)

    for contact in contact_list:
        
        text1.insert(END, contact)


########reset########
def Reset():
    Fname.set('')
    lname.set('')
    Number.set('')


########future login/logout/register (not priority)########


########define buttons########


btn1 = tk.Button(root, text="Add", font=('Arial',10), command=AddContact)
btn1.place(x=10, y=200)

btn2 = tk.Button(root, text="Remove", font=('Arial',10), command=remove )
btn2.place(x=45, y=200)

btn2 = tk.Button(root, text="Edit", font=('Arial',10), )
btn2.place(x=103, y=200)

btn2 = tk.Button(root, text="Show", font=('Arial',10), command = something)
btn2.place(x=138, y=200)

btn2 = tk.Button(root, text="Reset", font=('Arial',10), command=Reset)
btn2.place(x=182, y=200)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)




root.mainloop()#shows the GUI