def compress_string(sentence):

    liste = sentence.split()

    for i in range(len(liste)):

        nb = 0
        tmp = i+1

        try :
            while(liste[tmp] == liste[i]):
                nb += 1
                liste.pop(tmp)
        except :
            pass

        if nb > 0 :    
            liste[i] = liste[i]+ '(' + str(nb+1) + ')'

        res = " ".join(liste)

    return res


print(compress_string("yes yes yes please"))
print(compress_string("I have have have apples"))
print(compress_string("one one three and to the the the the"))
print(compress_string("route route route route route route tee tee tee tee tee tee"))