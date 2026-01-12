def golf_score(par, strokes):
    dico = { 2: "Eagle",
             1: "Birdie",
             0: "Par",
            -1: "Bogey",
            -2: "Double bogey"}

    if strokes == 1:
        return "Hole in one!"

    return dico[par-strokes]

print(golf_score(3, 3))
print(golf_score(4, 3))
print(golf_score(3, 1))
print(golf_score(5, 7))
print(golf_score(4, 5))
print(golf_score(5, 3))
