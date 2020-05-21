from tkinter import *
import server

def view_command():
    book_list.delete(0, END)
    for row in server.view():
        book_list.insert(END, row)

def search_command():
    book_list.delete(0, END)
    for row in server.search(title_text.get() ,author_text.get(), year_text.get(), isbn_text.get()):
        book_list.insert(END, row)

def add_command():
    server.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    book_list.delete(0, END)
    book_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def update_command():
    server.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def delete_command():
    server.delete(selected_tuple[0])

def get_selected_row(event):
    try:
        global selected_tuple
        index = book_list.curselection()[0]
        selected_tuple = book_list.get(index)
        entry_title.delete(0, END)
        entry_title.insert(END, selected_tuple[1])
        entry_author.delete(0, END)
        entry_author.insert(END, selected_tuple[2])
        entry_year.delete(0, END)
        entry_year.insert(END, selected_tuple[3])
        entry_isbn.delete(0, END)
        entry_isbn.insert(END, selected_tuple[4])
    except IndexError:
        pass

window = Tk()

label_title = Label(window, text = "Title: ")
label_title.grid(row = 1, column = 1)

label_author = Label(window, text = "Author: ")
label_author.grid(row = 1, column = 3)

label_year = Label(window, text = "Published On: ")
label_year.grid(row = 2, column = 1)

label_isbn = Label(window,text = "ISBN: ")
label_isbn.grid(row = 2,column = 3)

title_text = StringVar()
entry_title = Entry(window, textvariable = title_text, width = 48)
entry_title.grid(row = 1, column = 2)

author_text = StringVar()
entry_author = Entry(window, textvariable = author_text, width = 48)
entry_author.grid(row = 1, column = 4)

year_text = StringVar()
entry_year = Entry(window, textvariable = year_text, width = 48)
entry_year.grid(row = 2, column = 2)

isbn_text = StringVar()
entry_isbn = Entry(window, textvariable = isbn_text, width = 48)
entry_isbn.grid(row = 2, column = 4)

book_list = Listbox(window, height = 12, width = 64)
book_list.grid(row = 4, column = 1, rowspan = 8, columnspan = 2)

scrollbar = Scrollbar(window)
scrollbar.grid(row = 4, column = 3, rowspan = 8)

book_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = book_list.yview)

book_list.bind('<<ListboxSelect>>', get_selected_row)

button_view_all = Button(window, text = "View all", width = 12, command = view_command)
button_view_all.grid(row = 5, column = 4)

button_search = Button(window, text = "Search for entry", width = 12, command = search_command)
button_search.grid(row = 6, column = 4)

button_add = Button(window, text = "Add entry", width = 12, command = add_command)
button_add.grid(row = 7, column = 4)

button_update = Button(window, text = "Modify entry", width = 12, command = update_command)
button_update.grid(row = 8, column = 4)

button_delete = Button(window, text = "Remove entry", width = 12, command = delete_command)
button_delete.grid(row = 9, column = 4)

button_close = Button(window, text = "Close inventory", width = 12, command = window.destroy)
button_close.grid(row = 10, column = 4)

col_count, row_count = window.grid_size()

for col in range(col_count + 1):
    window.grid_columnconfigure(col, minsize = 20)

for row in range(row_count + 1):
    window.grid_rowconfigure(row, minsize = 20)

window.wm_title("isbn-py: Book Inventory")

window.mainloop()
