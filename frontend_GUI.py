"""
Program stores book information

Title, Author, Year, ISBN

User can:
View all records
Searchentry
Add entry
Update entry
Delete
Close

"""
from tkinter import *
import backend_GUI

# ----------Commands


def get_selected_row(event):
    try:
        global selected_tuple
        index = list.curselection()[0]
        selected_tuple = list.get(index)

    except IndexError:
        pass


def view_command():
    list.delete(0, END)
    for row in backend_GUI.view():
        list.insert(END, row)


def search_command():
    list.delete(0, END)
    for row in backend_GUI.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list.insert(END, row)


def add_command():
    backend_GUI.insert(title_text.get(), author_text.get(),
                       year_text.get(), isbn_text.get())
    list.delete(0, END)
    list.insert(END, (title_text.get(), author_text.get(),
                year_text.get(), isbn_text.get()))


def delete_command():
    backend_GUI.delete(selected_tuple[0])


def update_command():
    backend_GUI.update(selected_tuple[0], title_text.get(
    ), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()
window.wm_title("Bookstore")
# ----------Labels
title = Label(window, text="Title")
title.grid(row=0, column=0)

author = Label(window, text="Author")
author.grid(row=0, column=2)

year = Label(window, text="Year")
year.grid(row=1, column=0)

isbn = Label(window, text="ISBN")
isbn.grid(row=1, column=2)


# ----------Entry text box
title_text = StringVar()
etitle = Entry(window, textvariable=title_text)
etitle.grid(row=0, column=1)

author_text = StringVar()
eauthor = Entry(window, textvariable=author_text)
eauthor.grid(row=0, column=3)

year_text = StringVar()
eyear = Entry(window, textvariable=year_text)
eyear.grid(row=1, column=1)

isbn_text = StringVar()
eisbn = Entry(window, textvariable=isbn_text)
eisbn.grid(row=1, column=3)

# ----------List box
list = Listbox(window, height=6, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

list.bind('<<ListboxSelect>>', get_selected_row)

# ----------Scroll bar
sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

# ----------Buttons
view_b = Button(window, text="View all", width=12, command=view_command)
view_b.grid(row=2, column=3)

search_b = Button(window, text="Search entry",
                  width=12, command=search_command)
search_b.grid(row=3, column=3)

add_b = Button(window, text="Add entry", width=12, command=add_command)
add_b.grid(row=4, column=3)

update_b = Button(window, text="Update", width=12, command=update_command)
update_b.grid(row=5, column=3)

delete_b = Button(window, text="Delete",
                  width=12, command=delete_command)
delete_b.grid(row=6, column=3)

close_b = Button(window, text="Close", width=12, command=window.destroy)
close_b.grid(row=7, column=3)

window.mainloop()
