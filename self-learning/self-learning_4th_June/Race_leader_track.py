n = int(input("Enter number of racers: "))

fastest_time = float(input("Enter lap time of Racer 1: "))
slowest_time = fastest_time

fastest_pos = 1
slowest_pos = 1

for i in range(2, n + 1):
    time = float(input(f"Enter lap time of Racer {i}: "))

    if time < fastest_time:
        fastest_time = time
        fastest_pos = i

    if time > slowest_time:
        slowest_time = time
        slowest_pos = i

difference = slowest_time - fastest_time

print("Fastest Racer Position =", fastest_pos)
print("Slowest Racer Position =", slowest_pos)
print("Difference =", difference)