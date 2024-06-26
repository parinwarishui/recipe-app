import csv
import tkinter as tk
from tkinter import ttk
import foodlist
import random

######

root = tk.Tk()
root.title('Amazing Recipe Generator')

width = 1200
height = 800
root.geometry(f"{width}x{height}")
root.resizable(False, False)
root.configure(background='#ECEBC9')

# header
header = tk.Label(root, text='Amazing Recipe Generator', font='Arial 30 bold')
header.pack()

subtitle = tk.Label(root, text='WARNING, this is only for entertainment purposes, DO NOT attempt any of the generated recipes at home, please.', font='Arial 15')
subtitle.pack()

# select dish type - WILL IMPROVE LATER
choice1 = tk.StringVar(root)
choice1.set('Select Dish Type')
dish_option = tk.OptionMenu(root, choice1, *foodlist.dish_type)
dish_option.place(relx=0.2, rely=0.2, anchor=tk.W)

# randomly select one thing from all lists - will configure according to dish type later!
chosen_meat = random.choice(foodlist.animal_meats)
chosen_fruit = random.choice(foodlist.fruits)
chosen_veggie = random.choice(foodlist.leaf_veggies)
chosen_grain = random.choice(foodlist.grains)

root.mainloop()
