from tkinter import Button, Label
from gui_shop.helpers import clear_screen
from gui_shop.canvas import tk
from json import loads
from PIL import Image, ImageTk
import os

base_folder = os.path.dirname(__file__)


def buy_product(button):
    _, product_id = button.cget('text').split()
    product_id = int(product_id)
    print(product_id)
    pass


def render_products():
    clear_screen()
    with open('gui_shop/db/products.txt', 'r') as file:
        products = file.readlines()
        column_counter = 0
        for product in products:
            current_product = loads(product)
            Label(text=current_product.get('name')).grid(row=0, column=column_counter)
            image = Image.open(os.path.join(base_folder, 'images', current_product.get('img_name')))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=1, column=column_counter)
            button = Button(tk, text=f'Buy {current_product.get("id")}')
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=2, column=column_counter)
            column_counter += 1
