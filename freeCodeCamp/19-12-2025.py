def pairwise(arr, target):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                print(i)
                print(j)
                res += i + j
    return res/2

print(pairwise([2, 3, 4, 6, 8], 10))