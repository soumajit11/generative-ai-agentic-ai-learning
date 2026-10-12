import sys
from fractions import Fraction as f
from decimal import Decimal as d

ideal_temp = 95.5
current_temp = 95.499999999

print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Difference temp: {ideal_temp - current_temp}")
print(sys.float_info)