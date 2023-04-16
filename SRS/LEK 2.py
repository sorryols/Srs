def zad_1():
    lst = [4, -9, 8, -11, 8]
    count = len(list(filter(lambda x: x < 0, lst)))
    print(count)


def zad_2():
    players = ["Ashleigh Barty", "Simona Halep", "Naomi Osaka", "Karolina Pliskova", "Elina Svitolina"]

    players[0], players[-1] = players[-1], players[0]

    print(players)


def zad_3():
    message = "The reasonable man adapts himself to the world; the unreasonable one persists in trying to adapt the world to himself."
    words = message.split()

    for i in range(len(words)):
        if words[i] == "reasonable":
            words[i] = "unreasonable"
        elif words[i] == "unreasonable":
            words[i] = "reasonable"

    swapped_quote = " ".join(words)
    print(swapped_quote)
