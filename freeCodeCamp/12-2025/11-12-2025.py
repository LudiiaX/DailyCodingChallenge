def to_roman(num):
    temp = num
    dico = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
        }
    res = ''

    for n in dico:

        test = temp // n
        print(test)

        if test != 0 and test <= 3:
            res = res + test * dico[n]
            temp = temp - test * n
        print(res)
        
    
    return res


print(to_roman(18))
print(to_roman(19))
print(to_roman(1464))
print(to_roman(2025))
print(to_roman(3999))