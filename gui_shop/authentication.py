from tkinter import Button, Entry, Label
from gui_shop.canvas import tk
from gui_shop.helpers import clear_screen
from gui_shop.products import render_products
from json import dumps


def login(username, password):
    with open('gui_shop/db/user_credentials_db.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            user_name, pass_word = line[:-1].split(', ')
            if user_name == username and pass_word == password:
                render_products()
                return
        render_login(errors=True)
    pass


def register(**user):
    user.update({'products': []})
    with open('gui_shop/db/users.txt', 'a') as file:
        file.write(dumps(user))
        file.write('\n')
    with open('gui_shop/db/user_credentials_db.txt', 'a') as file:
        file.write(f'{user.get("username")}, {user.get("password")}')
        file.write('\n')
    render_login()


def render_register():
    clear_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk, show='*')
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


def render_login(errors=None):
    clear_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk, show='*')
    password.grid(row=1, column=0)
    Button(tk, text='Enter', bg='green', command=lambda: login(username=username.get(),
                                                               password=password.get())).grid(row=2, column=0)
    if errors:
        Label(tk, text='Invalid username or password').grid(row=3, column=0)


def render_main_enter_screen():
    Button(tk, text='Login', bg='green', fg='white', command=render_login).grid(row=0, column=0)
    Button(tk, text='Register', bg='yellow', command=render_register).grid(row=0, column=1)
