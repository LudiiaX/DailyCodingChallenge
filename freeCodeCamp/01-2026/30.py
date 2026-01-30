def find_pawn_moves(position):
    liste = list(position)
    print(liste)
    if int(liste[1]) == 2:
        return [liste[0]+str(int(liste[1])+1), liste[0]+str(int(liste[1])+2)]
    else:
        return [liste[0]+str(int(liste[1])+1)]

print(find_pawn_moves("D4"))
print(find_pawn_moves("B2"))
print(find_pawn_moves("A7"))
print(find_pawn_moves("G2"))
print(find_pawn_moves("E3"))

# 1 raw challenge:

def find_pawn_moves(p):
    return [p[0]+str(int(p[1])+1), p[0]+str(int(p[1])+2)] if p[1] == "2" else [p[0]+str(int(p[1])+1)]

print(find_pawn_moves("D4"))
print(find_pawn_moves("B2"))
print(find_pawn_moves("A7"))
print(find_pawn_moves("G2"))
print(find_pawn_moves("E3"))