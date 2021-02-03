from tkinter import Button, Entry
from gui_shop.canvas import tk
from gui_shop.helpers import clear_screen
from json import dumps
import os


def login():
    pass


def register(**user):
    print(os.getcwd())
    files = [f for f in os.listdir()]
    print(files)
    print(user)
    user.update({'products': []})
    with open('gui_shop/db/users.txt', 'a') as file:
        file.write(dumps(user))
        file.write('\n')


def render_register():
    clear_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=0)
    Button(tk, text='Register', bg='green',
           command=lambda: register(username=username.get(),
                                    password=password.get(),
                                    first_name=first_name.get(),
                                    last_name=last_name.get())).grid(row=4, column=0)


def render_login():
    clear_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)
    Button(tk, text='Enter', bg='green', command=login).grid(row=2, column=0)


def render_main_enter_screen():
    Button(tk, text='Login', bg='green', fg='white', command=render_login).grid(row=0, column=0)
    Button(tk, text='Register', bg='yellow', command=render_register).grid(row=0, column=1)
