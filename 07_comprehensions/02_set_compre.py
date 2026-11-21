favorite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

# Set implementation using comprehension by using { }
unique_chai = {chai for chai in favorite_chais}
print(unique_chai)

recipes = {
    "Masala Chai":["ginger", "cardamon", "clove"],
    "Elaichi Chai":["cardamon", "milk"],
    "Spicy Chai":["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)