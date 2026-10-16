def chai_flavour(flavour = "masal"):
    """Return the flavour of the chai""" # doc string or function documentation (1st line only)
    return flavour

# __ => dunder
# eg. - __doc__ => dunderdoc
print(chai_flavour.__doc__)
print(chai_flavour.__name__)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa
    :param chai: Number of chais cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    : return: (total amount, thank you message)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting our shop!"

generate_bill(5, 5)