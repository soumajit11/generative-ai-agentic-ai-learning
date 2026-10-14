# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing", order)

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling", "Yes", "Low") # positional arguments
make_chai(tea="Green", sugar="Medium", milk="No") # keyword arguments

def special_chai(*ingredients, **extras): # *args *kwargs
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardamon", sweetener="Honey", foam="Yes")


# def chai_order(order=[]): # Default trap
#     order.append("Masala")
#     print(order)

# chai_order()
# chai_order()

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()