def count_permutations(s):
    dico = {}
    #calculer la fréquence des lettres
    for i in s:
        if not i in dico:
            dico[i] = 0
        dico[i] += 1
    

    #mutiplie les factorielles de fréquence des lettres
    denom = 1
    for i in dico:
        denom *= factorielle(dico[i])

    #divise factorielle de la longueur par le denom
    res = factorielle(len(s)) // denom

    return res


def factorielle(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(count_permutations("abb"))         
print(count_permutations("abc"))          
print(count_permutations("racecar"))      
print(count_permutations("freecodecamp"))