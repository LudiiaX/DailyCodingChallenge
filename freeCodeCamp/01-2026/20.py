def to_consonant_case(s):
    vowels = ["a", "e", "i", "o", "u"]
    s = list(s)
    for i in range(len(s)):
        if s[i] == "-":
            s[i] = "_"
        elif s[i].lower() in vowels:
            s[i] = s[i].lower()
        else : 
            s[i] = s[i].upper()
    return "".join(s)

print(to_consonant_case("helloworld"))
print(to_consonant_case("HELLOWORLD"))
print(to_consonant_case("_hElLO-WOrlD-"))
print(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"))