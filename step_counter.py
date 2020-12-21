def calculate_steps(distance_m, steplength_m):
    return int(distance_m/steplength_m)

# 7km walk
print("You made", calculate_steps(distance_m=7000, steplength_m=1.39), "steps on that walk!")

# 9km walk
print("You made", calculate_steps(distance_m=9000, steplength_m=1.39), "steps on that walk!")
