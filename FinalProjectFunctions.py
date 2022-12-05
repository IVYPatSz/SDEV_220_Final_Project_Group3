from tkinter import *
import tkinter as tk


def reset():
    Fname.set('')
    Lname.set('')
    Number.set('')
    Email.set('')
    Country.set('')
    State.set('')
    City.set('')
    postCode.set('')
    Street.set('')


def remove():
    del contact_list[int(select.curselection()[0])]
    update_book()


def update_book():
    select.delete(0, END)
    for f,l,p,e,c,s,c,p,s in contact_list:
        select.insert(END, n)


def edit():
    