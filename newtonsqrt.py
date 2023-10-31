# Computing sqrt of a positive number c is equivalent
# to finding the positive root of the function f(x)=x**2-c
# This is the special case implemented here.
import math
# A variable defining the desired precision for the estimate
EPSILON = 1e-18

# Input the number you want to calculate the square root
c = float(input("number:"))
 
t = c # set the input as the initial value for the iteration
i = 1 # iteration counter

# if t=c/t then t is the square root of c
# The while loop as long as the difference t-c/t is larger then the
# desired precision 
while abs(t - c/t) > (EPSILON * t):
    # Replace t by the average of t and c/t.
    print("Iteration ",i, ", Estimate: ", t)
    t = (c/t + t) / 2.0
    i=i+1

print("\n Final result:",t)
print(" math.sqrt(c)=",math.sqrt(c))