def to_snake(camel):
    camel = list(camel)
    res = []
    for i in range(len(camel)):
        if camel[i].isupper():
            res.append("_")
            res.append(camel[i].lower())
        else:
            res.append(camel[i])
    res = "".join(res)
    return res

print(to_snake("helloWorld"))
print(to_snake("myVariableName"))
print(to_snake("freecodecampDailyChallenges"))