def title_case(title):

    liste = list(title)

    premier = True
    for i in range(len(liste)):
        if premier == True:
            liste[i] = liste[i].upper()
            premier = False
        else :
            liste[i] = liste[i].lower()

        if liste[i] == " ":
            premier = True
    print(liste)

    title = ''.join(liste)
    return title


print(title_case("hello world"))
print(title_case("the quick brown fox"))
print(title_case("JAVASCRIPT AND PYTHON"))
print(title_case("AvOcAdO tOAst fOr brEAkfAst"))