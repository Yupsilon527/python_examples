from tkinter import *
from backend import Database

db = Database("books.db")

def view_cmd():
    booklist.delete(0,END)
    for row in db.view():
        booklist.insert(END,row)

def search_cmd():
    booklist.delete(0,END)
    for row in db.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        booklist.insert(END,row)

def insert_cmd():
    db.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_cmd()

def get_selected_row(event):
    global selection
    try:
        index = booklist.curselection()[0]
        selection = booklist.get(index)

        inputA.delete(0,END)
        inputA.insert(0,selection[1])

        inputB.delete(0,END)
        inputB.insert(0,selection[2])

        inputC.delete(0,END)
        inputC.insert(0,selection[3])

        inputD.delete(0,END)
        inputD.insert(0,selection[4]) 

        view_cmd()
    except IndexError:
        pass

def update_cmd():
    try:
        db.updatedata(selection[0],selection[1],selection[2],selection[3],selection[4]) 
        view_cmd()
    except NameError:
        pass
        
def delete_cmd():
    db.delete(selection[0])
    view_cmd()

window = Tk()
window.wm_title("Book Library")

title = Label(window,text="Title")
title.grid(row=0,column=0)

author = Label(window,text="Author")
author.grid(row=0,column=2)

year = Label(window,text="Year")
year.grid(row=1,column=0)

isbn = Label(window,text="ISBN")
isbn.grid(row=1,column=2)

title_text = StringVar()
inputA = Entry(window,textvariable=title_text)
inputA.grid(row=0,column=1)

author_text = StringVar()
inputB = Entry(window,textvariable=author_text)
inputB.grid(row=0,column=3)

year_text = StringVar()
inputC = Entry(window,textvariable=year_text)
inputC.grid(row=1,column=1)

isbn_text = StringVar()
inputD = Entry(window,textvariable=isbn_text)
inputD.grid(row=1,column=3)

booklist = Listbox(window, height = 6,width = 12)
booklist.grid(row=2,column=0,rowspan=6,columnspan=2)
booklist.bind("<<ListboxSelect>>",get_selected_row)

bookscroll = Scrollbar(window)
bookscroll.grid(row=1,column=3,rowspan = 6)

booklist.configure(yscrollcommand = bookscroll.set)
bookscroll.configure(command = booklist.yview)

btn1 = Button(window,text="View All",command = view_cmd)
btn1.grid(row=2,column=3)  

btn2 = Button(window,text="Search",command= search_cmd)
btn2.grid(row=3,column=3)  

btn3 = Button(window,text="Add",command = insert_cmd)
btn3.grid(row=4,column=3)  

btn4 = Button(window,text="Update",command = update_cmd)
btn4.grid(row=5,column=3)  

btn5 = Button(window,text="Delete", command = delete_cmd)
btn5.grid(row=6,column=3)  

btn6 = Button(window,text="Close",command = window.destroy)
btn6.grid(row=7,column=3)  

view_cmd()
window.mainloop()