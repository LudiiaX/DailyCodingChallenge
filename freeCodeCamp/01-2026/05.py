def tire_status(pressures_psi, range_bar):
    converted = []
    for i in range_bar:
        converted.append(i * 14.5038)

    res = []
    print(converted)
    for i in pressures_psi:
        if i < converted[0]:
            res.append("Low")
        elif i > converted[0] and i < converted[1]:
            res.append("Good")
        elif i > converted[1]:
            res.append("High")

    return res

print(tire_status([32, 28, 35, 29], [2, 3]))
print(tire_status([32, 28, 35, 30], [2, 2.3]))
print(tire_status([29, 26, 31, 28], [2.1, 2.5]))
print(tire_status([29, 26, 31, 28], [2.1, 2.5]))
print(tire_status([31, 31, 30, 29], [1.5, 2]))
print(tire_status([30, 28, 30, 29], [1.9, 2.1]))