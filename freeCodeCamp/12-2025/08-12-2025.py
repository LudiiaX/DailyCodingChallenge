def convert_to_kgs(lbs):
    kg = round(0.453592 * lbs, 2)

    kgs = str(kg)
    if kgs.endswith(".0"):
        kgs = f"{kg:.2f}"
    

    p_unit = "pound" if lbs == 1 else "pounds"
    k_unit = "kilogram" if kgs == "1.00" else "kilograms"
    
    return str(lbs) + " " + p_unit +" equals " + str(kgs) + " " + k_unit + "."

print(convert_to_kgs(1))
print(convert_to_kgs(0))
print(convert_to_kgs(100))
print(convert_to_kgs(2.5))
print(convert_to_kgs(2.20462))