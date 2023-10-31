import random

n = int(input("n="))
v_min = 1.
v_max = 0.
v_sum = 0.

for _ in range(n):
    v = random.random()
    v_sum += v
    
    if v < v_min:
        v_min = v
    if v > v_max:
        v_max = v
        
print(f"Average: {v_sum/n}")
print(f"Minimum: {v_min}")
print(f"Maximum: {v_max}")
