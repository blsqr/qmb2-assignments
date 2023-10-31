# Import some functions that we need
from math import sqrt, sin, cos, radians

# Get inputs from the user
alpha = float(input("What angle are you throwing at? [°]    "))
v0 = float(input("What speed are you throwing at? [m/s]  "))
h = float(input("What height are you throwing from? [m] "))
g = 9.81

# Do the computations
v0_sin_alpha = v0 * sin(radians(alpha))
t_flight = v0_sin_alpha + sqrt(v0_sin_alpha ** 2 + 2*g*h) / g
d = v0 * cos(radians(alpha)) * t_flight

# Communicate results
print(f"The distance thrown:     {d:.4g} m")
print(f"The time of flight is:   {t_flight:.4g} s")
