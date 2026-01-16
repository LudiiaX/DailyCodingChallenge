def get_number_of_plants(field_size, unit, crop):
    dico = {"corn": 1,
            "wheat": 0.1,
            "soybeans": 0.5,
            "tomatoes": 0.25,
            "lettuce": 0.2}
            
    if unit == "acres":
        field_size = field_size*4046.86
    elif unit == "hectares":
        field_size = field_size*10000
    
    return int(field_size/dico[crop])

print(get_number_of_plants(1, "acres", "corn"))
print(get_number_of_plants(2, "hectares", "lettuce"))
print(get_number_of_plants(20, "acres", "soybeans"))
print(get_number_of_plants(3.75, "hectares", "tomatoes"))
print(get_number_of_plants(16.75, "acres", "tomatoes"))