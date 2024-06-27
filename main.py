import csv
import tkinter as tk
from tkinter import ttk, messagebox
import foodlist
import random

######

root = tk.Tk()
root.title('Amazing Recipe Generator')

width = 1200
height = 1000
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
    if selected == "dessert":

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

        string_desserts_ingredients = (
            f"230g {vegetables1} oil\n"
            f"100g natural yogurt\n"
            f"large eggs\n"
            f"1½ tsp vanilla extract\n"
            f"½ {fruits1}, zested\n"
            f"265g {grains1} flour\n"
            f"335g {seasoning1}\n"
            f"2½ tsp {seasoning2}\n"
            f"¼ fresh {nuts1}, finely grated\n"
            f"265g {fruits2}, grated\n"
            f"100g {fruits3}\n"
            f"100g {nuts2}, roughly chopped\n"
            f"100g slightly salted butter, softened\n"
            f"300g {seasoning3}\n"
            f"100g {seasoning4}"
        )

        if 'ingredients_label' in globals():
            ingredients_label.config(text=string_desserts)
        else:
            ingredients_label = tk.Label(root, text=string_desserts_ingredients, font='Arial 12', wraplength=1000, justify=tk.LEFT)
            ingredients_label.pack(pady=10)

        string_desserts = (f"STEP 1\n"
                f"Heat the oven to 180C.\n" 
                f"Oil and line the base and sides of two 20cm cake tins with baking parchment.\n"
                f"Whisk the {vegetables1} oil, yogurt, eggs, vanilla and {fruits1} zest in a jug. Mix the flour, {seasoning1}, {seasoning2} and {nuts1} with a good pinch of salt in a bowl. \n"
                f"Squeeze any lumps of {seasoning1} through your fingers, shaking the bowl a few times to bring the lumps to the surface.\n"
                f"STEP 2\n"
                f"Add the wet ingredients to the dry, along with the {fruits2}, {fruits3} and half the {nuts2}.\n"
                f"Mix well to combine, then divide between the tins.\n"
                f"STEP 3\n"
                f"Bake for 25-30 mins or until a skewer inserted into the centre of the cake comes out clean. \n"
                f"If any wet mixture clings to the skewer, return to the oven for 5 mins, then check again.\n"
                f"Leave to cool in the tins.\n"
                f"STEP 4\n"
                f"To make the icing, beat the butter and {seasoning3} together until smooth. \n"
                f"Add half the {seasoning4} and beat again, then add the rest (adding it bit by bit prevents the icing from splitting). \n"
                f"Remove the cakes from the tins and sandwich together with half the icing.\n"
                f"Top with the remaining icing and scatter with the remaining {nuts2}. \n"
                f"Will keep in the fridge for up to five days. Best eaten at room temperature.\n")
        
        if 'recipe_label' in globals():
            recipe_label.config(text=string_desserts)
        else:
            recipe_label = tk.Label(root, text=string_desserts, font='Arial 12', wraplength=1000, justify=tk.LEFT)
            recipe_label.pack(pady=10)


#############

# header
header = tk.Label(root, text='Amazing Recipe Generator', font='Arial 30 bold')
header.pack()

subtitle = tk.Label(root, text='WARNING, this is only for entertainment purposes, DO NOT attempt any of the generated recipes at home, please.', font='Arial 15')
subtitle.pack()

choice1 = tk.StringVar(root)
choice1.set('Select Dish Type')
dish_option = tk.OptionMenu(root, choice1, *foodlist.dish_type)
dish_option.place(relx=0.2, rely=0.2, anchor=tk.W)

submit_button = ttk.Button(root, text="Submit", command=on_click)
submit_button.pack(pady=20)

############

root.mainloop()
