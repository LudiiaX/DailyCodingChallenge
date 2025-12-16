def has_consonant_count(text, target):
    con = ["a", "e", "i", "o", "u"]
    liste = list(text)
    count = 0
    for i in liste:
        if i.isalpha() and i not in con:
            count += 1

    if count == target:
        return True
    return False

print(has_consonant_count("helloworld", 7))
print(has_consonant_count("eieio", 5))
print(has_consonant_count("freeCodeCamp Rocks!", 11))
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24))
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23))