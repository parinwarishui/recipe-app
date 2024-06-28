import tkinter as tk
from tkinter import ttk
import foodlist
import random

######

root = tk.Tk()
root.title('Amazing Recipe Generator')
background_color = '#ECEBC9'

width = 1200
height = 1000
root.geometry(f"{width}x{height}")
root.configure(background=background_color)

main_animal_meats = foodlist.animal_meats
main_leaf_veggies = foodlist.leaf_veggies
main_grains = foodlist.grains
main_fruits = foodlist.fruits
main_seasoning = foodlist.seasoning
main_nuts = foodlist.nuts
string_ingredients_header = "Ingredients:"

# custom repeat function to remove old ones, to not repeat ingredients in the SAME recipe.
def random_norepeat(list):
    if not list:
        print("No more elements to choose from.") 
        return None
    choice = random.choice(list)
    list.remove(choice)
    return choice

# function to reset the lists back to normal after each recipe generation, to allow repeating ingredients in DIFFERENT recipes.
def reset_all_lists():
    global animal_meats, leaf_veggies, grains, fruits, seasoning, nuts
    animal_meats = main_animal_meats[:]
    leaf_veggies = main_leaf_veggies[:]
    grains = main_grains[:]
    fruits = main_fruits[:]
    seasoning = main_seasoning[:]
    nuts = main_nuts[:]

# function to check submission
def on_click():
    choice = choice1.get()
    show_recipe(choice)

# function to generate recipes based on choice
def show_recipe(selected):
    if selected == "cake":
        vegetables1 = random_norepeat(leaf_veggies)
        fruits1 = random_norepeat(fruits)
        fruits2 = random_norepeat(fruits)
        fruits3 = random_norepeat(fruits)
        seasoning1 = random_norepeat(seasoning)
        seasoning2 = random_norepeat(seasoning)
        seasoning3 = random_norepeat(seasoning)
        seasoning4 = random_norepeat(seasoning)
        seasoning5 = random_norepeat(seasoning)
        grains1 = random_norepeat(grains)
        nuts1 = random_norepeat(nuts)
        nuts2 = random_norepeat(nuts)

        string_cake_ingredients = (
            f"230g {vegetables1} oil\n"
            f"100g natural yogurt\n"
            f"½ {fruits1}, zested\n"
            f"265g {grains1} flour\n"
            f"335g {seasoning1}\n"
            f"large eggs\n"
            f"1½ tsp {seasoning5}\n"
            f"2½ tsp {seasoning2}\n"
            f"¼ fresh {nuts1}, finely grated\n"
            f"265g {fruits2}, grated\n"
            f"100g {fruits3}\n"
            f"100g {nuts2}, roughly chopped\n"
            f"100g slightly salted butter, softened\n"
            f"300g {seasoning3}\n"
            f"100g {seasoning4}"
        )

        string_cake_name = (f"{fruits2} cake(?)")

        string_cake = (f"STEP 1\n"
        f"Heat the oven to 180C.\n" 
        f"Oil and line the base and sides of two 20cm cake tins with baking parchment.\n"
        f"Whisk the {vegetables1} oil, yogurt, eggs, {seasoning5} and {fruits1} zest in a jug.\n"
        f"Mix the flour, {seasoning1}, {seasoning2} and {nuts1} with a good pinch of salt in a bowl.\n"
        f"Squeeze any lumps of {seasoning1} through your fingers, shaking the bowl a few times to bring the lumps to the surface.\n"
        f"STEP 2\n"
        f"Add the wet ingredients to the dry, along with the {fruits2}, {fruits3} and half the {nuts2}.\n"
        f"Mix well to combine, then divide between the tins.\n"
        f"STEP 3\n"
        f"Bake for 25-30 mins or until a skewer inserted into the centre of the cake comes out clean.\n"
        f"If any wet mixture clings to the skewer, return to the oven for 5 mins, then check again.\n"
        f"Leave to cool in the tins.\n"
        f"STEP 4\n"
        f"To make the icing, beat the butter and {seasoning3} together until smooth.\n"
        f"Add half the {seasoning4} and beat again, then add the rest (adding it bit by bit prevents the icing from splitting).\n"
        f"Remove the cakes from the tins and sandwich together with half the icing.\n"
        f"Top with the remaining icing and scatter with the remaining {nuts2}.\n"
        f"Will keep in the fridge for up to five days. Best eaten at room temperature.\n")

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        ingredients_name = tk.Label(scrollable_frame, text=string_cake_name, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_name.pack(pady=10)

        recipe_image = tk.PhotoImage(file="cake.png")
        image_label = tk.Label(scrollable_frame, image=recipe_image, background=background_color)
        image_label.pack(pady=10)
        image_label.image = recipe_image

        ingredients_header_label = tk.Label(scrollable_frame, text=string_ingredients_header, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_header_label.pack(pady=10)

        ingredients_label = tk.Label(scrollable_frame, text=string_cake_ingredients, font=('Comic Sans MS', 15), wraplength=1000, justify=tk.LEFT, background=background_color, fg='black')
        ingredients_label.pack(pady=10)

        recipe_label = tk.Label(scrollable_frame, text=string_cake, font=('Comic Sans MS', 10), background=background_color, wraplength=1000, justify=tk.LEFT, fg='black')
        recipe_label.pack(pady=10)

    elif selected == "stir-fry":
        meat1 = random_norepeat(animal_meats)
        grains1 = random_norepeat(grains)
        grains2 = random_norepeat(grains)
        seasoning1 = random_norepeat(seasoning)
        seasoning2 = random_norepeat(seasoning)
        seasoning3 = random_norepeat(seasoning)
        seasoning4 = random_norepeat(seasoning)
        vegetables1 = random_norepeat(leaf_veggies)
        fruits1 = random_norepeat(fruits)
        nuts1 = random_norepeat(nuts)

        string_stirfry_ingredients = (
            f"2 nests medium egg noodles\n"
            f"2 tsp {grains1} flour\n"
            f"2 tbsp {seasoning1}\n"
            f"1 tbsp {seasoning2}\n"
            f"1 tbsp {nuts1} oil\n"
            f"250g/9oz {meat1}, cut into bite-sized pieces\n"
            f"thumb-sized piece {seasoning3}\n"
            f"2 {seasoning4}, finely chopped\n"
            f"1 {fruits1}, deseeded and sliced\n"
            f"100g {vegetables1}\n"
            f"1 tsp {grains2}"
        )

        string_stirfry_name = f"stir-fried {meat1}(?)"

        string_stirfry = (
            f"STEP 1\n"
            f"Bring a pan of salted water to the boil and cook the noodles following pack instructions.\n"
            f"Meanwhile, mix the {grains1} flour with 1 tbsp water, then stir in the {seasoning1} and {seasoning2}, and set aside.\n"
            f"STEP 2\n"
            f"Heat the oil in a wok over a high heat. Add the {meat1} and cook for 2 mins until browned all over.\n"
            f"Add the {seasoning3}, {seasoning4}, {fruits1} and {vegetables1}, and cook for a further 2 mins.\n" 
            f"Reduce the heat, then add the {seasoning1} and {seasoning2} mixture, stirring and cooking until the sauce bubbles and thickens.\n" 
            f"Divide the drained noodles between 2 bowls. Top with the {meat1} and {vegetables1}, and finish with a sprinkling of {grains2}.\n"
        )

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        ingredients_name = tk.Label(scrollable_frame, text=string_stirfry_name, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_name.pack(pady=10)

        recipe_image = tk.PhotoImage(file="stirfry.png")
        image_label = tk.Label(scrollable_frame, image=recipe_image, background=background_color)
        image_label.pack(pady=10)
        image_label.image = recipe_image

        ingredients_header_label = tk.Label(scrollable_frame, text=string_ingredients_header, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_header_label.pack(pady=10)

        ingredients_label = tk.Label(scrollable_frame, text=string_stirfry_ingredients, font=('Comic Sans MS', 15), wraplength=1000, justify=tk.LEFT, background=background_color, fg='black')
        ingredients_label.pack(pady=10)

        recipe_label = tk.Label(scrollable_frame, text=string_stirfry, font=('Comic Sans MS', 10), background=background_color, wraplength=1000, justify=tk.LEFT, fg='black')
        recipe_label.pack(pady=10)

    elif selected == "salad":
        vegetables1 = random_norepeat(leaf_veggies)
        vegetables2 = random_norepeat(leaf_veggies)
        fruits1 = random_norepeat(fruits)
        fruits2 = random_norepeat(fruits)
        seasoning1 = random_norepeat(seasoning)
        seasoning2 = random_norepeat(seasoning)
        grains1 = random_norepeat(grains)
        grains2 = random_norepeat(grains)

        string_salad_ingredients = (
            f"2 large {fruits2}\n"
            f"1½ tbsp wholegrain {grains1}\n"
            f"1½ tsp {seasoning1}\n"
            f"1 tbsp {seasoning2}\n"
            f"3 tbsp {grains2} oil, plus extra for frying\n"
            f"2 large {fruits1}, peeled\n"
            f"225g {vegetables1}, sliced\n"
            f"100g bag {vegetables2}\n"
        )

        string_salad_name = (f"{vegetables1}, {fruits1} & {fruits2} salad(?)")

        string_salad = (
            f"STEP 1\n"
            f"Cut the peel and pith away from the {fruits2}.\n"
            f"Use a small serrated knife to segment the {fruits2}, catching any juices in a bowl,\n" 
            f"then squeeze any excess juice from the off-cut pith into the bowl as well.\n" 
            f"Add the {grains1}, {seasoning1}, {seasoning2}, {grains2} oil to the bowl and mix well.\n"

            f"STEP 2\n"
            f"Using a vegetable peeler, peel {fruits1} ribbons into the dressing bowl and toss gently.\n"
            f"Heat a drizzle of oil in a frying pan and cook the {vegetables1} for a few mins until golden on both sides.\n"
            f"Toss the watercress through the dressed {fruits1}.\n"
            f"Arrange the {vegetables2} mixture on plates and top with the {vegetables1} and {fruits2}.\n"
        )

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        ingredients_name = tk.Label(scrollable_frame, text=string_salad_name, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_name.pack(pady=10)

        recipe_image = tk.PhotoImage(file="salad.png")
        image_label = tk.Label(scrollable_frame, image=recipe_image, background=background_color)
        image_label.pack(pady=10)
        image_label.image = recipe_image

        ingredients_header_label = tk.Label(scrollable_frame, text=string_ingredients_header, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_header_label.pack(pady=10)

        ingredients_label = tk.Label(scrollable_frame, text=string_salad_ingredients, font=('Comic Sans MS', 15), wraplength=1000, justify=tk.LEFT, background=background_color, fg='black')
        ingredients_label.pack(pady=10)

        recipe_label = tk.Label(scrollable_frame, text=string_salad, font=('Comic Sans MS', 10), background=background_color, wraplength=1000, justify=tk.LEFT, fg='black')
        recipe_label.pack(pady=10)

    elif selected == "sandwich":
        vegetables1 = random_norepeat(leaf_veggies)
        vegetables2 = random_norepeat(leaf_veggies)
        fruits1 = random_norepeat(fruits)
        fruits2 = random_norepeat(fruits)
        seasoning1 = random_norepeat(seasoning)
        seasoning2 = random_norepeat(seasoning)
        meat1 = random_norepeat(animal_meats)
        meat2 = random_norepeat(animal_meats)
        nuts1 = random_norepeat(nuts)
        nuts2 = random_norepeat(nuts)

        string_sandwich_ingredients = (
            f"1 tbsp {nuts1} oil\n"
            f"1 {fruits1}, finely chopped\n"
            f"150ml {fruits2} wine\n"
            f"300g {meat2} stock\n"
            f"1 large baguette\n"
            f"½-1 tbsp {seasoning1}\n"
            f"100g cold roast {meat1}\n"
            f"½ small pack {vegetables1}, finely chopped\n"
            f"1 tbsp {nuts2}, finely chopped\n"
            f"1 tbsp {seasoning2}\n"
            f"handful {vegetables2}, to serve\n"
        )

        string_sandwich_name = (f"{meat1} sandwich(?)")

        string_sandwich = f"""
            STEP 1
            Heat oven to 180C.
            Pour the oil into a small saucepan over a medium heat,
            add the {fruits1} with a pinch of salt and cook, stirring frequently,
            for 5 mins until softened and beginning to caramelise.
            STEP 2
            Tip in the wine, cook for a couple of mins until reduced by half,
            then pour in the stock. Leave to bubble for 15-20 mins
            until you have a thick gravy.
            STEP 3
            Put the baguette in the oven for 5 mins to warm up and crisp, then
            cut in half lengthways. Spread one half with {seasoning1} and top with
            the roast {meat1}.
            STEP 4
            Add the {vegetables1}, {nuts2} and {seasoning2} to the gravy.
            Season to taste, then spoon the gravy over the other half of the baguette,
            scattering over some {vegetables2}. Halve, divide between two plates,
            then eat straight away, with more gravy on the side.
            """

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        ingredients_name = tk.Label(scrollable_frame, text=string_sandwich_name, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_name.pack(pady=10)

        recipe_image = tk.PhotoImage(file="sandwich.png")
        image_label = tk.Label(scrollable_frame, image=recipe_image, background=background_color)
        image_label.pack(pady=10)
        image_label.image = recipe_image

        ingredients_header_label = tk.Label(scrollable_frame, text=string_ingredients_header, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
        ingredients_header_label.pack(pady=10)

        ingredients_label = tk.Label(scrollable_frame, text=string_sandwich_ingredients, font=('Comic Sans MS', 15), wraplength=1000, justify=tk.LEFT, background=background_color, fg='black')
        ingredients_label.pack(pady=10)

        recipe_label = tk.Label(scrollable_frame, text=string_sandwich, font=('Comic Sans MS', 10), background=background_color, wraplength=1000, justify=tk.LEFT, fg='black')
        recipe_label.pack(pady=10)

    reset_all_lists() #reset all ingredients lists

#############

# header
header = tk.Label(root, text='Amazing Recipe Generator', font=('Comic Sans MS', 30, 'bold'), background=background_color, fg='black')
header.pack()

# warning quote
subtitle = tk.Label(root, text='WARNING, this is only for entertainment purposes, DO NOT attempt any of the generated recipes at home, please.', font=('Comic Sans MS', 15),background=background_color, fg='black')
subtitle.pack()

# Question and choice frame
frame_top = tk.Frame(root, background=background_color)
frame_top.pack(pady=10)

question = tk.Label(frame_top, text='What type of dish would you like?', font=('Comic Sans MS', 15), background=background_color, fg='black')
question.pack()

choice1 = ttk.Combobox(frame_top, values=foodlist.dish_type, font=('Comic Sans MS', 12))
choice1.set('Select a dish type')
choice1.pack(pady=5)

submit_button = tk.Button(frame_top, text='Submit', font=('Comic Sans MS', 12), command=on_click)
submit_button.pack()

# scrollable frame that shows recipe
recipe_frame = tk.Frame(root, background=background_color)
recipe_frame.place(relx=0.5, rely=0.55, anchor='center', width=850, height=600)

border_frame = tk.Frame(recipe_frame, background="black", bd=5)
border_frame.pack(expand=True, fill="both", padx=5, pady=5)

canvas = tk.Canvas(border_frame, background=background_color, borderwidth=0, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, background=background_color)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollbar = ttk.Scrollbar(border_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

############

reset_all_lists()
root.mainloop()
