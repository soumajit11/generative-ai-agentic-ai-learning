#Tuples are immutable
masala_spices = ("cardamon", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamon_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cardamon_ratio}")
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio #Swapping values
print(f"Ratio is G: {ginger_ratio} and C: {cardamon_ratio}")

#membership
print(f"Is cinnamon in masala spices ? {'Cinnamon' in masala_spices}") #Case-Sensitve