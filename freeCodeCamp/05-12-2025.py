def difference(arr1, arr2):
    diff = []
    for i in arr1:
        if i not in arr2:
            diff.append(i)

    for i in arr2:
        if i not in arr1:
            diff.append(i)
    return diff


print(difference([1, 2, 3], [3, 4, 5]))
print(difference(["a", "b"], ["c", "b"]))
print(difference([1, "a", 2], [2, "b", "a"]))
print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))