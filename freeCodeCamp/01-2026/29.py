def separate_letters_and_numbers(s):
    res = [s[0]]
    for i in range(1, len(s)):
        before = s[i-1].isdigit()
        after = s[i].isdigit()
        if before != after:
            res.append("-")
            res.append(s[i])
        else:
            res.append(s[i])  
    return "".join(res)

print(separate_letters_and_numbers("ABC123"))
print(separate_letters_and_numbers("Route66"))
print(separate_letters_and_numbers("H3LL0W0RLD"))
print(separate_letters_and_numbers("a1b2c3d4"))

# 1 raw challenge:
def separate_letters_and_numbers(s):
    return "".join([s[0]]+["-"+s[i] if s[i-1].isdigit() != s[i].isdigit() else s[i] for i in range(1, len(list(s)))])

print(separate_letters_and_numbers("ABC123"))
print(separate_letters_and_numbers("Route66"))
print(separate_letters_and_numbers("H3LL0W0RLD"))
print(separate_letters_and_numbers("a1b2c3d4"))