def convert_to_km(miles):
    k =  round(1.60934 * miles, 2)
    return k

print(convert_to_km(1))
print(convert_to_km(21))
print(convert_to_km(3.5))
print(convert_to_km(0))
print(convert_to_km(0.621371))