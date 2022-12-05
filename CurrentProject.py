#Final project sketch
#address book

import select
import tkinter as tk
from tkinter import ttk
from tkinter import END, VERTICAL, Listbox, Scrollbar, StringVar, Text, simpledialog
#imports everything from tkinter


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
postCode = StringVar()
street = StringVar()




########FUNCTIONS########



########inputs######## -Jordy [working]
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




########ADD FUNCTION######## - Jordy [working]
class ADD:
    def AddContact():
        contact_list.append([Fname.get(), Lname.get(), Number.get(), Email.get(), Country.get(), State.get(), City.get(), postCode.get(), Street.get()])
        print(*contact_list)
    
    btn1 = tk.Button(root, text="Add", font=('Arial',10), command= AddContact)
    btn1.place(x=10, y=250)

########REMOVE FUCTION######## - Samuel
# def remove():
#     del contact_list[int(select.curselection()[0])]
#     update_book()

########EDIT FUNCTION########


########SHOW FUNCTION######## -Jordy [testing]


# def Show_List():
#     print("First Name: %s\nLast Name: %s \nNumber: %s \nEmail: %s \nCountry: %s \nState: %s \nCity: %s \npostCode: %s \nStreet: %s" % (Fname.get(), Lname.get(), Number.get(), Email.get(), Country.get(), State.get(), City.get(), postCode.get(), Street.get())  
#     )
class SHOW:
    def Show_conct():
        text1=tk.Text(root, width=20, height=15)
        text1.place(x=300, y=0)
    

        for contact in contact_list:
            text1.insert(END, contact)
    btn2 = tk.Button(root, text="Show", font=('Arial',10), command = Show_conct)
    btn2.place(x=181, y=250)






########RESET FUNCTION######## - Samuel [testing]
# def reset():
#      Fname.set('')
#      Lname.set('')
#      Number.set('')
#      Email.set('')
#      Country.set('')
#      State.set('')
#      City.set('')
#      postCode.set('')
#      Street.set('')

########UPTADE############ - Samuel [testing]
# def update_book():
#     select.delete(0, END)
#     for f,l,p,e,c,s,c,p,s in contact_list:
#         select.insert(END, n)

########future login/logout/register (not priority)########


########define buttons######## - Patrick/Jordy - [working]
#These are temporary until a class is made
btn2 = tk.Button(root, text="Remove", font=('Arial',10),) #command=remove )
btn2.place(x=60, y=250)

btn2 = tk.Button(root, text="Edit", font=('Arial',10), )
btn2.place(x=130, y=250)

btn2 = tk.Button(root, text="Reset", font=('Arial',10),) #command=Reset)
btn2.place(x=240, y=250)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)



root.mainloop()#shows the GUI