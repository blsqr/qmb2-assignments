import math

numbers = [2**p for p in range(1,12)]

for n in numbers:
    print(f"{math.log2(n):4.3g}  {n:4}  {n*math.log(n):10.3f}  {n**2:10d}  {n**3:12d}")