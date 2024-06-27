import csv
import tkinter as tk
from tkinter import ttk, messagebox
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

main_animal_meats = foodlist.animal_meats
main_leaf_veggies = foodlist.leaf_veggies
main_grains = foodlist.grains
main_fruits = foodlist.fruits
main_seasoning = foodlist.seasoning
main_nuts = foodlist.nuts

# custom repeat function to remove old ones
def random_norepeat(list):
    if not list:
        print("No more elements to choose from.")
        return None
    choice = random.choice(list)
    list.remove(choice)
    return choice

# function to check submission
def on_click():
    choice = choice1.get()
    if choice == "dessert":
        show_recipe(choice)


def show_recipe(selected):
    new_win = tk.Toplevel(root)
    new_win.title("Selected Nut")
    tk.Label(new_win, text=f"You selected: {selected}").pack(pady=10)
    
    # Add specific conditions based on selected nut
    if selected == "dessert":
        tk.Label(new_win, text=string_dessert).pack(pady=10)
        print(string_dessert)

#############

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

submit_button = ttk.Button(root, text="Submit", command=on_click)
submit_button.pack(pady=20)

# randomly select one thing from all lists - will configure according to dish type later!
# dessert - will input condition later
def random_total_dessert():
    global vegetables1, fruits1, fruits2, fruits3, seasoning1, seasoning2, seasoning3, seasoning4, grains1, nuts1, nuts2
    vegetables1 = random_norepeat(main_leaf_veggies)
    fruits1 = random_norepeat(main_fruits)
    fruits2 = random_norepeat(main_fruits)
    fruits3 = random_norepeat(main_fruits)
    seasoning1 = random_norepeat(main_seasoning)
    seasoning2 = random_norepeat(main_seasoning)
    seasoning3 = random_norepeat(main_seasoning)
    seasoning4 = random_norepeat(main_seasoning)
    grains1 = random_norepeat(main_grains)
    nuts1 = random_norepeat(main_nuts)
    nuts2 = random_norepeat(main_nuts)

string_desserts = ("STEP 1"
"Heat the oven to 180C/160C fan/gas 4." 
"Oil and line the base and sides of two 20cm cake tins with baking parchment. "
f"Whisk the {vegetables1} oil, yogurt, eggs, vanilla and zest in a jug. Mix the flour, {seasoning1}, {seasoning2} and {nuts1} with a good pinch of salt in a bowl. "
f"Squeeze any lumps of {seasoning1} through your fingers, shaking the bowl a few times to bring the lumps to the surface."
"STEP 2"
f"Add the wet ingredients to the dry, along with the {fruits2}, {fruits3} and half the {nuts2}. "
"Mix well to combine, then divide between the tins."
"STEP 3"
"Bake for 25-30 mins or until a skewer inserted into the centre of the cake comes out clean. "
"If any wet mixture clings to the skewer, return to the oven for 5 mins, then check again. "
"Leave to cool in the tins."
"STEP 4"
f"To make the icing, beat the butter and {seasoning3} together until smooth. "
f"Add half the {seasoning4} and beat again, then add the rest (adding it bit by bit prevents the icing from splitting). "
"Remove the cakes from the tins and sandwich together with half the icing. "
f"Top with the remaining icing and scatter with the remaining {nuts2}. "
"Will keep in the fridge for up to five days. Best eaten at room temperature.")

root.mainloop()
