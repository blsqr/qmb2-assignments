vmin = 1000
vmax = 2000
n_per_line = 5

for n in range(vmin, vmax):
    print(f"{n:4d}", end=" ")
    if n % n_per_line == 0:
        print("")