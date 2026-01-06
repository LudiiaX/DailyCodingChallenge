def vowel_case(s):
    vowels = ["a", "e", "i", "o", "u"]
    s = list(s)
    for i in range(len(s)):
        if s[i] in vowels or s[i].lower() in vowels:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()

    return "".join(s)

print(vowel_case("vowelcase"))
print(vowel_case("coding is fun"))
print(vowel_case("HELLO, world!"))
print(vowel_case("git cherry-pick"))
print(vowel_case("HEAD~1"))