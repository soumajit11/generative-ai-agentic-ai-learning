# Hiding the implementation to understand the dataflow better

def get_input():
    print("Getting user input")

def validate_input():
    print("Validating user information")

def save_to_db():
    print("Saving to Database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")

register_user()
