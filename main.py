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
    # declare general variables
    global string_name, string_ingredients, string_steps, recipe_image
    adjective1 = random.choice(foodlist.adjectives)

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

        string_ingredients = (
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

        string_name = (f"{adjective1} {fruits2} cake(?)")

        string_steps = (f"STEP 1\n"
        f"Heat the oven to 180C.\n" 
        f"Oil and line the base and sides of two 20cm cake tins with baking parchment.\n"
        f"Whisk the {vegetables1} oil, yogurt, eggs, {seasoning5} and {fruits1} zest in a jug.\n"
        f"Mix the flour, {seasoning1}, {seasoning2} and {nuts1} with a good pinch of salt in a bowl.\n"
        f"Squeeze any lumps of {seasoning1} through your fingers, shaking the bowl a few times to bring the lumps to the surface.\n\n"
        f"STEP 2\n"
        f"Add the wet ingredients to the dry, along with the {fruits2}, {fruits3} and half the {nuts2}.\n"
        f"Mix well to combine, then divide between the tins.\n\n"
        f"STEP 3\n"
        f"Bake for 25-30 mins or until a skewer inserted into the centre of the cake comes out clean.\n"
        f"If any wet mixture clings to the skewer, return to the oven for 5 mins, then check again.\n"
        f"Leave to cool in the tins.\n\n"
        f"STEP 4\n"
        f"To make the icing, beat the butter and {seasoning3} together until smooth.\n"
        f"Add half the {seasoning4} and beat again, then add the rest (adding it bit by bit prevents the icing from splitting).\n"
        f"Remove the cakes from the tins and sandwich together with half the icing.\n"
        f"Top with the remaining icing and scatter with the remaining {nuts2}.\n"
        f"Will keep in the fridge for up to five days. Best eaten at room temperature.\n")

        recipe_image = tk.PhotoImage(file="cake.png")

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

        string_ingredients = (
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

        string_name = f"{adjective1} stir-fried {meat1}(?)"

        string_steps = (
            f"STEP 1\n"
            f"Bring a pan of salted water to the boil and cook the noodles following pack instructions.\n"
            f"Meanwhile, mix the {grains1} flour with 1 tbsp water, then stir in the {seasoning1} and {seasoning2}, and set aside.\n\n"
            f"STEP 2\n"
            f"Heat the oil in a wok over a high heat. Add the {meat1} and cook for 2 mins until browned all over.\n"
            f"Add the {seasoning3}, {seasoning4}, {fruits1} and {vegetables1}, and cook for a further 2 mins.\n" 
            f"Reduce the heat, then add the {seasoning1} and {seasoning2} mixture, stirring and cooking until the sauce bubbles and thickens.\n" 
            f"Divide the drained noodles between 2 bowls. Top with the {meat1} and {vegetables1}, and finish with a sprinkling of {grains2}.\n"
        )

        recipe_image = tk.PhotoImage(file="stirfry.png")

    elif selected == "salad":
        vegetables1 = random_norepeat(leaf_veggies)
        vegetables2 = random_norepeat(leaf_veggies)
        fruits1 = random_norepeat(fruits)
        fruits2 = random_norepeat(fruits)
        seasoning1 = random_norepeat(seasoning)
        seasoning2 = random_norepeat(seasoning)
        grains1 = random_norepeat(grains)
        grains2 = random_norepeat(grains)
        adjective1 = random.choice(foodlist.adjectives)

        string_ingredients = (
            f"2 large {fruits2}\n"
            f"1½ tbsp wholegrain {grains1}\n"
            f"1½ tsp {seasoning1}\n"
            f"1 tbsp {seasoning2}\n"
            f"3 tbsp {grains2} oil, plus extra for frying\n"
            f"2 large {fruits1}, peeled\n"
            f"225g {vegetables1}, sliced\n"
            f"100g bag {vegetables2}\n"
        )

        string_name = (f"{adjective1} {vegetables1}, {fruits1} & {fruits2} salad(?)")

        string_steps = (
            f"STEP 1\n"
            f"Cut the peel and pith away from the {fruits2}.\n"
            f"Use a small serrated knife to segment the {fruits2}, catching any juices in a bowl,\n" 
            f"then squeeze any excess juice from the off-cut pith into the bowl as well.\n" 
            f"Add the {grains1}, {seasoning1}, {seasoning2}, {grains2} oil to the bowl and mix well.\n\n"
            f"STEP 2\n"
            f"Using a vegetable peeler, peel {fruits1} ribbons into the dressing bowl and toss gently.\n"
            f"Heat a drizzle of oil in a frying pan and cook the {vegetables1} for a few mins until golden on both sides.\n"
            f"Toss the watercress through the dressed {fruits1}.\n"
            f"Arrange the {vegetables2} mixture on plates and top with the {vegetables1} and {fruits2}.\n"
        )

        recipe_image = tk.PhotoImage(file="salad.png")

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

        string_ingredients = (
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

        string_name = (f"{adjective1} {meat1} sandwich(?)")

        string_steps = f"""
            STEP 1
            Heat oven to 180C.
            Pour the oil into a small saucepan over a medium heat,
            add the {fruits1} with a pinch of salt and cook, stirring frequently,
            for 5 mins until softened and beginning to caramelise.\n
            STEP 2
            Tip in the wine, cook for a couple of mins until reduced by half,
            then pour in the stock. Leave to bubble for 15-20 mins
            until you have a thick gravy.\n
            STEP 3
            Put the baguette in the oven for 5 mins to warm up and crisp, then
            cut in half lengthways. Spread one half with {seasoning1} and top with
            the roast {meat1}.\n
            STEP 4
            Add the {vegetables1}, {nuts2} and {seasoning2} to the gravy.
            Season to taste, then spoon the gravy over the other half of the baguette,
            scattering over some {vegetables2}. Halve, divide between two plates,
            then eat straight away, with more gravy on the side.
            """

        recipe_image = tk.PhotoImage(file="sandwich.png")
        
    elif selected == "soup":
        vegetables1 = random_norepeat(leaf_veggies)
        vegetables2 = random_norepeat(leaf_veggies)
        vegetables3 = random_norepeat(leaf_veggies)
        vegetables4 = random_norepeat(leaf_veggies)
        seasoning1 = random_norepeat(seasoning)
        meat1 = random_norepeat(animal_meats)
        grains1 = random_norepeat(grains)

        string_ingredients = (f"""
            90g butter
            2 medium {vegetables2}, roughly chopped
            {seasoning1}
            500g {vegetables1}, finely chopped
            2 tbsp {grains1} flour
            1l hot {meat1} stock
            1 {vegetables3}
            4 tbsp single cream
            small handful flat-leaf {vegetables4}
        """)

        string_name = (f"{adjective1} {vegetables1} soup(?)")

        string_steps = f"""
            STEP 1
            Heat the butter in a large saucepan and cook the {vegetables2} and {seasoning1} until soft 
            but not browned, about 8-10 mins.\n
            STEP 2
            Add the {vegetables1} and cook over a high heat for another 3 mins until softened. 
            Sprinkle over the flour and stir to combine. Pour in the {meat1} stock, 
            bring the mixture to the boil, then add the {vegetables3} and simmer for another 10 mins.\n
            STEP 3
            Remove and discard the {vegetables3}, then remove the {vegetables1} mixture from the heat 
            and blitz using a hand blender until smooth. Gently reheat the soup and stir through the cream 
            (or, you could freeze the soup at this stage – simply stir through the cream when heating). 
            Scatter over the {vegetables4}, if you like, and serve.
            """

        recipe_image = tk.PhotoImage(file="soup.png")
    
    elif selected == "noodles":
        vegetables1 = random_norepeat(leaf_veggies)
        fruits1 = random_norepeat(fruits)
        seasoning1 = random_norepeat(seasoning)
        meat1 = random_norepeat(animal_meats)
        grains1 = random_norepeat(grains)
        nuts1 = random_norepeat(nuts)
        nuts2 = random_norepeat(nuts)

        string_ingredients = (f"""
            4 tbsp {seasoning1}
            4 tbsp {fruits1} wine
            1 {nuts1}, finely chopped
            1 {nuts2}, crushed
            2 {meat1} fillets
            140g noodles
            2 tbsp {grains1}
            2 {vegetables1}, chopped
        """)

        string_name = (f"{adjective1} {meat1} noodles(?)")

        string_steps = f"""
            STEP 1
            Heat the oven to 180C/160C fan/gas 4. In a small jug, whisk together the {seasoning1}, 
            {fruits1} wine, {nuts1}, and {nuts2}. Line a roasting tin with 
            baking parchment and put the {meat1} in it. Pour over half the sauce, then bake 
            for 15 mins until the {meat1} is cooked through.\n
            STEP 2
            Meanwhile, bring a large pan of water to the boil. Add the noodles and cook 
            following pack instructions, then drain well.\n
            STEP 3
            In a small frying pan, lightly toast the {grains1} for 1 min, then add to the
            cooked noodles (reserving a sprinkle for the top). Pour the remaining sauce over 
            the noodles, plus any from the roasting tin, and toss together. Serve with the 
            {meat1}, scattered with the chopped {vegetables1} and remaining {grains1}.
            """
        
        recipe_image = tk.PhotoImage(file="noodles.png")
    
    elif selected == "pie":
        fruits1 = random_norepeat(fruits)
        fruits2 = random_norepeat(fruits)
        fruits3 = random_norepeat(fruits)
        seasoning1 = random_norepeat(seasoning)
        seasoning2 = random_norepeat(seasoning)
        grains1 = random_norepeat(grains)
        grains2 = random_norepeat(grains)
        nuts1 = random_norepeat(nuts)

        string_ingredients = (f"""
            300g {grains1} flour
            200g cold salted butter, cut into cubes
            1 tsp {fruits2} vinegar
            1 egg, beaten
            {seasoning1}
            1.2kg {fruits1} peeled, stoned and cut into chunks
            150g {seasoning2}
            60g {grains2} flour, plus extra for dusting
            1 {fruits3}, juiced
            20g {nuts1}, peeled and sliced
        """)

        string_name = (f"{adjective1} {fruits1} pie(?)")

        string_steps = f"""
            STEP 1
            Tip the flour into a large bowl and toss with the butter. 
            Mix the butter into the flour using two forks until you have medium lumps of butter 
            coated in flour. Add the vinegar, then slowly add 120ml ice-cold water, 1 tbsp at a time, 
            mixing well until you have a shaggy dough.

            STEP 2
            Turn the dough out onto a surface and fold it onto itself a few times until you have a 
            pliable dough with streaks of butter throughout. If it feels dry, dampen your hands lightly 
            and continue to fold. If it’s sticky, sprinkle over a little more flour. When it’s cohesive, 
            divide it in two and flatten into discs. Wrap and chill for 2 hrs, or overnight.

            STEP 3
            For the filling, combine the {fruits1}, {seasoning2}, {grains2} flour, {fruits3} juice and {nuts1} in a large bowl.

            STEP 4
            Roll out each pastry disc into a 30cm circle on a lightly floured surface. 
            Use one to line a 23cm pie dish, smoothing it to the edges. Heat the oven to 220C/200C fan/gas 7.

            STEP 5
            Cut the second pastry circle into 12 x 2.5cm-wide strips using a pizza cutter.
            Weave the strips into a lattice by arranging six vertically parallel to each other on a board 
            or sheet of baking parchment with a space between each. Partially fold back alternate strips, 
            then lay another horizontally across the top, near the folds. Flip the folded strips back over 
            to cover the horizontal ones. Repeat with the process, alternating which vertical strips are 
            folded down each time.

            STEP 6
            Pour the filling into the pastry case. Brush some beaten egg over the edge of the pie crust, 
            then top with the lattice, press around the edge to seal, then crimp using a fork. 
            Brush over the rest of the egg, then cover it with {seasoning1}.

            STEP 7
            Bake at 220C/200C fan/gas 7 for 30 mins, then turn the oven down to 200C/180C fan/gas 6 for 45 mins more, 
            loosely covering with foil if it gets too dark. Leave to cool for 1 hr so the juices can set before slicing.
            """
        
        recipe_image = tk.PhotoImage(file="pie.png")

    elif selected == "pizza":
        fruits1 = random_norepeat(fruits)
        fruits2 = random_norepeat(fruits)
        fruits3 = random_norepeat(fruits)
        grains1 = random_norepeat(grains)
        meat1 = random_norepeat(animal_meats)
        vegetables1 = random_norepeat(leaf_veggies)
        vegetables2 = random_norepeat(leaf_veggies)
        vegetables3 = random_norepeat(leaf_veggies)

        string_ingredients = (f"""
            10g fresh yeast or 7g sachet dried
            ½ tsp sugar
            375g {grains1} flour, plus extra for dusting
            1 tbsp {vegetables1} oil, plus extra for greasing
            375g {meat1}
            fresh {vegetables3}, to serve
            3 tbsp {vegetables2} oil
            1 {fruits1}, chopped
            1 {fruits3}, crushed
            2 x 400g cans good-quality Italian chopped {fruits2}
        """)

        string_name = (f"{adjective1} {meat1} pizza")

        string_steps = f"""
            STEP 1
            Mix together the yeast and sugar with 250ml warm water and leave to sit for 10 mins. 
            Place half the flour in a table-top mixer with a dough hook, pour in the yeast mixture 
            and beat at medium speed for 10 mins (or mix in a bowl, then knead with oiled hands in 
            the bowl for 5-10 mins).

            STEP 2
            Leave somewhere warm for 10 more mins, then add the remaining flour and oil. 
            Beat or knead to a dough for a further 5 mins. Put in a well-oiled bowl, 
            cover with a cloth and place somewhere warm to double in size – about 1½ hrs.

            STEP 3
            For the sauce, heat the {vegetables2} oil in a pan over a moderate heat. 
            Add the {fruits1} and cook for 3 mins, stirring constantly. 
            Add the {fruits3}, 1 tsp sea salt and 1 tsp ground black pepper and cook for 2 mins more. 
            Add the {fruits2} and bring to the boil, then reduce the heat and simmer for a good 
            20 mins, stirring occasionally.

            STEP 4
            Once your dough has doubled in size, slap it down on a lightly floured surface and knead 
            for 4 mins until soft but not too elastic. Divide into 6 pieces, roll into balls and leave to rest for 10 mins. 
            Heat oven to the highest temperature possible (270C fan in the Good Food test kitchen) 
            and place a flat baking sheet in the oven.

            STEP 5
            With a well-floured rolling pin, roll out each ball of dough as thinly as possible. 
            Remove the baking sheet from the oven, oil or dust with flour, then carefully transfer the dough base onto it. 
            Spread over some of the {fruits2} sauce, then the {meat1} and any toppings you desire.

            STEP 6
            Cook for between 5-10 mins depending on your oven temp, 
            until the base is crisp and the {meat1} cooked. Scatter with {vegetables3}.
            """
        
        recipe_image = tk.PhotoImage(file="pizza.png")

    elif selected == "curry":
        fruits1 = random_norepeat(fruits)
        fruits2 = random_norepeat(fruits)
        meat1 = random_norepeat(animal_meats)
        meat2 = random_norepeat(animal_meats)
        vegetables1 = random_norepeat(leaf_veggies)
        seasoning1 = random_norepeat(seasoning)
        seasoning2 = random_norepeat(seasoning)
        seasoning3 = random_norepeat(seasoning)
        seasoning4 = random_norepeat(seasoning)

        string_ingredients = (f"""
            2 tbsp oil
            500g diced braising {meat1}
            1 tbsp butter
            1 large onion, chopped
            2 garlic cloves, crushed
            1 thumb sized piece of {fruits2}, finely grated
            ¼ tsp {seasoning1}
            1 tsp {seasoning2}
            2 tsp {seasoning3}
            3 {seasoning4}, crushed
            400g can chopped {fruits1}
            300ml {meat2} stock
            1 tsp sugar
            2 tsp garam masala
            2 tbsp double cream (optional)
            ½ small bunch {vegetables1}, roughly chopped
            naan bread or rice, to serve
        """)

        string_name = (f"{adjective1} {meat1} curry")

        string_steps = f"""
            STEP 1
            Heat one tbsp of the oil in a casserole pot over a medium-high heat. 
            Season the {meat1} and fry in the pot for 5-8 mins, turning with a pair 
            of tongs half way until evenly browned. Set aside on a plate.

            STEP 2
            Heat the remaining oil and butter in the pan and add the onions. 
            Fry gently for 15 mins or until golden brown and caramelised. 
            Add the garlic, {fruits2}, {seasoning1}, {seasoning2}, {seasoning3} and {seasoning4}
            and fry for two mins. Tip in the {fruits1}, stock and sugar and bring to the simmer.

            STEP 3
            Add the {meat1}, put a lid on top of the curry and cook over a low heat 
            for 1 ½ – 2 hrs or until the meat is tender and falling apart. 
            Remove the lid for the last 20 minutes of cooking.

            STEP 4
            Stir through the garam masala and cream (if using) and season to taste. 
            Scatter over the {vegetables1} and serve with naan breads or rice.
            """
        
        recipe_image = tk.PhotoImage(file="curry.png")

    # create the text labels and images

    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    header_label = tk.Label(scrollable_frame, text=string_name, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
    header_label.pack(pady=10)

    image_label = tk.Label(scrollable_frame, image=recipe_image, background=background_color)
    image_label.pack(pady=10)
    image_label.image = recipe_image

    ingredients_header_label = tk.Label(scrollable_frame, text=string_ingredients_header, font=('Comic Sans MS', 20, 'bold'), background=background_color, fg='black')
    ingredients_header_label.pack(pady=10)

    ingredients_label = tk.Label(scrollable_frame, text=string_ingredients, font=('Comic Sans MS', 15), wraplength=1000, justify=tk.LEFT, background=background_color, fg='black')
    ingredients_label.pack(pady=10)

    recipe_label = tk.Label(scrollable_frame, text=string_steps, font=('Comic Sans MS', 10), background=background_color, wraplength=1000, justify=tk.LEFT, fg='black')
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
