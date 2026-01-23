def get_average_grade(scores):
    dico = {
            "A+": [97, 100],
            "A": [93, 96],
            "A-": [90, 92],
            "B+": [87, 89],
            "B": [83, 86],
            "B-": [80, 82],
            "C+": [77, 79],
            "C": [73, 76],
            "C-": [70, 72],
            "D+": [67, 69],
            "D": [63, 66],
            "D-": [60, 62],
            "F": [0, 59]
            }
    score = round(sum(scores)/len(scores))
    
    for i in dico:
        if score >= dico[i][0] and score <= dico[i][1]:
            return i

print(get_average_grade([92, 91, 90, 94, 89, 93]))
print(get_average_grade([84, 89, 85, 100, 91, 88, 79]))
print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))
print(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]))
print(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]))
print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]))
