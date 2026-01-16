def parse_unordered_list(markdown):
    liste = markdown.split("\n")

    for i in range(len(liste)) :
        count = 0

        for j in range(len(liste[i])):
            print(liste[i][j])
            if not liste[i][j].isalnum():
                count += 1
            else:
                break
        liste[i] = "<li>" + liste[i][count:] + "</li>"

    

    return "<ul>" + "".join(liste) + "</ul>"

print(parse_unordered_list("- Item A\n- Item B"))
print(parse_unordered_list("-  JavaScript\n-  Python"))
print(parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla"))
print(parse_unordered_list("- A-1\n- A-2\n- B-1"))