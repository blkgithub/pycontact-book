from tkinter import *
from functions import *

# Main window
root = Tk()
root.geometry("400x520")
root.title("Contact Book")

# Buttons
Button(
    root,
    text="Contact List",
    font=("italic", 10),
    bg="white",
    command=lambda: selectAll(root),
).place(x=140, y=70)

Button(
    root,
    text="Add Contact",
    font=("italic", 10),
    bg="white",
    command=lambda: addContact(root),
).place(x=140, y=140)

# Not Implemented Yet
Button(
    root, text="Search Contact", state=DISABLED, font=("italic", 10), bg="white"
).place(x=140, y=210)

# Not Implemented Yet
Button(
    root, text="Modify Contact", state=DISABLED, font=("italic", 10), bg="white"
).place(x=140, y=280)

# Not Implemented Yet
Button(
    root, text="Delete Contact", state=DISABLED, font=("italic", 10), bg="white"
).place(x=140, y=350)

Button(root, text="Exit", font=("italic", 10), bg="white", command=root.destroy).place(
    x=140, y=420
)

mainloop()
