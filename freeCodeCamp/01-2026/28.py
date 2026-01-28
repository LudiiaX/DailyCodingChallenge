def flatten(arr):
    res = []
    for i in arr:
        if type(i) != list:
            res.append(i)
        else :
            res = res + flatten(i)

    return res

print(flatten([1, [2, 3], 4]))
print(flatten([5, [4, [3, 2]], 1]))
print(flatten(["A", [[[["B"]]]], "C"]))
print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))