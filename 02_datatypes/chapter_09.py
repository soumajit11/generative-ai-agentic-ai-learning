essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# | - pipe operator also known as union operator
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# & - used for intersection in sets
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in essential spices: {'cloves' in optional_spices}")

