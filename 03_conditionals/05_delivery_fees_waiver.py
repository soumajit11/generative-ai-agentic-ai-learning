order_mount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_mount > 300 else 30

print(f"Delivery fees is : {delivery_fees}")