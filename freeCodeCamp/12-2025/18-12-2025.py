def create_board(dimensions):
    res = []
    

    for i in range(0, dimensions[0]):
        temp = []
        if i == 0:
            X = True
        else :
            if res[i-1][0] == "X":
                X = False
            else :
                X = True
        for j in range(0, dimensions[1]):
            if X:
                temp.append("X")
                X = not X
            else :
                temp.append("O")
                X = not X
        res.append(temp)

    return res


print(create_board([3, 3]))
print(create_board([6, 1]))
print(create_board([2, 10]))
print(create_board([5, 4]))