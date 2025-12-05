def read(file = "input_01.txt"):
    command = []
    with open(file, "r") as f:
        for ligne in f:
            command.append(ligne.strip())

    return command


if __name__ == '__main__':
    current = 50
    command = read()
    counter = 0
    print(command)
    for i in command:
        d = i[0]
        n = int(i[1:])
        
        if d == "L":
            current = (current - n)
        elif d == "R":
            current = (current + n)

        if current < 0 or 100 < current:
            counter += 1
            
            current = current % 100
            print("The dial is rotated ", i, " to point at ", n, "; during this rotation, it points at 0 once.")


        if current == 0:
            counter += 1
            print("The dial is rotated ", i ," to point at ", n ,".")

    print(counter)