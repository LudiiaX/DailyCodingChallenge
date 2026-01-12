def most_frequent(arr):
    dico = {}
    #compter les fréquences
    for i in arr:
        if i in dico: 
            dico[i] += 1
        else :
            dico[i] = 1 
    
    #trouver la plus grande
    best = {"score": 0, "name": None}
    for i in dico:
        if dico[i] > best["score"]:
            best["score"] = dico[i]
            best["name"] = i


    return best["name"]



print(most_frequent(["a", "b", "a", "c"]))
print(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]))
print(most_frequent([True, False, "False", "True", False]))
print(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]))