# importing the necessary modules

import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector


root = Tk()
root.title("BOOK ISSUING SYSTEM")

# creating the database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='library'
)

# creating the cursor object
cursor = connection.cursor()

bkg = "#636e72"
frame = tk.Frame(root, bg=bkg)


label_book_id = tk.Label(frame, text="Book ID: ", font=('verdana',12), bg=bkg)
entry_book_id = tk.Entry(frame, font=('verdana',12))

label_book_name = tk.Label(frame, text="Title: ", font=('verdana',12), bg=bkg)
entry_book_name = tk.Entry(frame, font=('verdana',12))

label_book_author = tk.Label(frame, text="Author: ", font=('verdana',12), bg=bkg)
entry_book_author = tk.Entry(frame, font=('verdana',12))

label_issue_date = tk.Label(frame, text="Issue Date: ", font=('verdana',12), bg=bkg)
entry_issue_date = tk.Entry(frame, font=('verdana',12))

label_return_date = tk.Label(frame, text="Return Date: ", font=('verdana',12), bg=bkg)
entry_return_date = tk.Entry(frame, font=('verdana',12))


def add_book():
    book_id = entry_book_id.get()
    book_name = entry_book_name.get()
    book_author = entry_book_author.get()
    issue_date = entry_issue_date.get()
    return_date = entry_return_date.get()

    insert_query = "INSERT INTO `books`(`book_id`, `book_name`, `book_author`, `issue_date`, `return_date`) VALUES (%s,%s,%s,%s,%s)"
    vals = (book_id, book_name, book_author,  issue_date, return_date)
    cursor.execute(insert_query, vals)
    connection.commit()

button_insert = tk.Button(frame, text='Insert', font=('verdana', 14), bg='orange', command=add_book)
button_issue = tk.Button(frame, text='Issue', font=('verdana', 14), bg='orange')
button_return = tk.Button(frame, text='Return', font=('verdana', 14), bg='orange')
button_available = tk.Button(frame, text='Available', font=('verdana', 14), bg='orange')

'''
def book_issuing():
    book_id = entry_book_id.get()
    book_name = entry_book_name.get()
    book_author = entry_book_author.get()
    issue_date = entry_issue_date.get()
    return_date = entry_return_date.get()

    update_query = "UPDATE books SET book_id = %s, book_name = %s, book_author = %s, issue_date = %s, return_date = %s WHERE book_id = %s"
    vals = (book_id, book_name, book_author,  issue_date, return_date, book_id)
    cursor.execute(update_query, vals)
    connection.commit()

button_issue = tk.Button(frame, text='Issue', font=('verdana', 14), bg='orange', command=book_issuing)


def issue():

    
    button_issue = tk.Button(frame, text='Issue', font=('verdana', 14), bg='orange')
'''




label_book_id.grid(row=0, column=0)
entry_book_id.grid(row=0, column=1, pady=10, padx=10, sticky='e')

label_book_name.grid(row=1, column=0)
entry_book_name.grid(row=1, column=1, pady=10, padx=10, sticky='e')

label_book_author.grid(row=2, column=0)
entry_book_author.grid(row=2, column=1, pady=10, padx=10, sticky='e')

label_issue_date.grid(row=3, column=0)
entry_issue_date.grid(row=3, column=1, pady=10, padx=10, sticky='e')

label_return_date.grid(row=4, column=0)
entry_return_date.grid(row=4, column=1, pady=10, padx=10, sticky='e')

button_insert.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="snew")
button_issue.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="snew")
button_return.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky="snew")
button_available.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="snew")

frame.grid(row=0, column=0)
root.mainloop()