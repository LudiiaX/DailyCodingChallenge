def parse_bold(markdown):
    liste = markdown.split(" ")

    for i in range(len(liste)):
        
        if liste[i] == "**" or liste[i] == "__":
            return markdown

        elif len(liste[i]) >= 2:
            if liste[i][:2] == "**" or liste[i][:2] == "__":
                liste[i] = "<b>" + liste[i][2:]
                
            if liste[i][-2:] == "**" or liste[i][-2:] == "__":
                liste[i] = liste[i][:-2] + "</b>"


    return " ".join(liste)


print(parse_bold("**This is bold**"))
print(parse_bold("__This is also bold__"))
print(parse_bold("**This is not bold **"))
print(parse_bold("__ This is also not bold__"))
print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))