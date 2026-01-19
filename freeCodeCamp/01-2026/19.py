def compare_energy(calories_burned, watt_hours_used):
    w = 4184 * calories_burned
    d = 3600 * watt_hours_used
    if w>d:
        return "Workout"
    elif d>w: 
        return "Devices"
    else : 
        return "Equal"

print(compare_energy(250, 50))
print(compare_energy(100, 200))
print(compare_energy(450, 523))
print(compare_energy(300, 75))
print(compare_energy(200, 250))
print(compare_energy(900, 1046))