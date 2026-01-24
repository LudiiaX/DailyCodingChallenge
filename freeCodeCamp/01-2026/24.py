def get_bingo_letter(n):
    dico = {
        "B": [1,15],
        "I": [16,30],
        "N": [31,45],
        "G": [46,60],
        "O": [61,75],
    }

    for i in dico:
        if n>=dico[i][0] and n<=dico[i][1]:
            return i


print(get_bingo_letter(75))
print(get_bingo_letter(54))
print(get_bingo_letter(25))
print(get_bingo_letter(38))
print(get_bingo_letter(11))