import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as MessageBox


def selectAll(master):
    newWindow = Toplevel(master)
    newWindow.title("Contact List")
    newWindow.geometry("650x300")

    # Connect to the mysql localhost, with a "python" database previously created.
    con = mysql.connect(host="localhost", user="root", password="", database="python")
    cursor = con.cursor()
    cursor.execute("SELECT name, surname, phone FROM contact_book")
    data = cursor.fetchall()

    # Make the grid
    frm = Frame(newWindow)
    frm.pack(side=tk.LEFT, padx=20)
    tv = ttk.Treeview(frm, columns=(1, 2, 3), show="headings", height="5")
    tv.heading(1, text="Name")
    tv.heading(2, text="Surname")
    tv.heading(3, text="Phone Number")
    tv.pack()
    for i in data:
        tv.insert("", "end", values=i)


def add(window, name, surname, phone):
    # Connect to the mysql localhost, with a "python" database previously created.
    con = mysql.connect(host="localhost", user="root", password="", database="python")
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO contact_book(name,surname,phone) VALUES('"
        + name
        + "','"
        + surname
        + "','"
        + phone
        + "')"
    )
    cursor.execute("commit")
    con.close()
    MessageBox.showinfo("Notice", "Contact successfully added to the contact book")
    window.destroy()


def addContact(master):
    newWindow = Toplevel(master)
    newWindow.title("Add Contact")
    newWindow.geometry("450x300")

    # Make the contact form
    # Labels
    Label(newWindow, text="Name", font=("bold", 10)).place(x=50, y=30)
    Label(newWindow, text="Surname", font=("bold", 10)).place(x=50, y=60)
    Label(newWindow, text="Phone Number", font=("bold", 10)).place(x=50, y=90)

    # Inputs
    e_name = Entry(newWindow)
    e_name.place(x=160, y=30)
    e_surname = Entry(newWindow)
    e_surname.place(x=160, y=60)
    e_phone = Entry(newWindow)
    e_phone.place(x=160, y=90)

    insert = Button(
        newWindow,
        text="Save",
        font=("italic", 10),
        bg="white",
        command=lambda: add(newWindow, e_name.get(), e_surname.get(), e_phone.get()),
    )
    insert.place(x=20, y=140)
