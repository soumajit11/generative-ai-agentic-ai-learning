# pure function - no global variable use
def pure_chai(cups):
    return cups * 10

# impure function - using global variable - not recommended
total_chai = 0
def impure_chai(cups):
    global total_chai
    total_chai += cups

# recursive function
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))

# lambda functions: anonymous functions
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))