def parse_blockquote(markdown):
    liste =list(markdown)
    print(liste)

    count = 0
    for i in range(len(liste)):
        if not liste[i].isalpha():
            count += 1
        else:
            break

    prefix = liste[0:count]
    suffixe = liste[count:]

    if ">" in prefix:
        return "<blockquote>"+"".join(suffixe)+"</blockquote>"

    return "Not a blockquote"


print(parse_blockquote("> This is a quote"))
print(parse_blockquote(" > This is also a quote"))
print(parse_blockquote("  >    So  Is  This"))