# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:50:45 2017

@author: Dante

The program makes use of a database to store information on books current attributes
are Title(e1), Author(e2), Year(e3), ISBN(e4).

User can:
    View records
    Update records
    Add records
    Search records
    Delete records
    Close the application
"""

from tkinter import *
import Backend as bd

def get_selected_row(event):
    '''
    The rows from the database are populated within a textfield. Information
    is pulled from the highlighted entry and populated within Entry boxes.
    '''
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    '''
    Clears listbox and populates it with all the rows from the table using view
    method defined in backend.
    '''
    list1.delete(0,END)
    for row in bd.view():
        list1.insert(END,row)

def search_command():
    '''
    Clears listbox and calls search from backend, textfield is populated from results.
    '''
    list1.delete(0,END)
    for row in bd.search(e1val.get(),e2val.get(),e3val.get(),e4val.get()):
        list1.insert(END,row)

def add_command():
    '''
    Creates a new entry and calls add from backend. Adds row with desired parameters to the bottom of the table.
    '''
    bd.add(e1val.get(),e2val.get(),e3val.get(),e4val.get())
    list1.delete(0,END)
    list1.insert(END,(e1val.get(),e2val.get(),e3val.get(),e4val.get()))

def delete_command():
    '''
    Deletes selected row from the textfield.
    '''
    bd.delete(selected_tuple[0])

def update_command():
    '''
    Calls update from backend and updates relevant tuple with new information.
    '''
    bd.update(selected_tuple[0],e1val.get(),e2val.get(),e3val.get(),e4val.get())

#GUI is created here
window = Tk()

window.wm_title("Bookstore")

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

e1val = StringVar()
e1 = Entry(window, textvariable=e1val)
e1.grid(row=0, column=1)

e2val = StringVar()
e2 = Entry(window, textvariable=e2val)
e2.grid(row=0, column=3)

e3val = StringVar()
e3 = Entry(window, textvariable=e3val)
e3.grid(row=1, column=1)

e4val = StringVar()
e4 = Entry(window, textvariable=e4val)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=15, command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text="Search Entry", width=15, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add Entry", width=15, command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window, text="Update Selected", width=15, command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text="Delete Selected", width=15, command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window, text="Close", width=15, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()



























