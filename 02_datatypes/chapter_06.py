#Strings are immutable
chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Reverse: {chai_description[::-1]}")

label_text = "Chai Spécial"
encoded_text = label_text.encode("utf-8")
print(f"Non Encoded Label: {label_text}")
print(f"Encoded label: {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded Label: {decoded_text}")