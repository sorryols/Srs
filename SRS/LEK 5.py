def zad_1():
    num = int(input("Enter num"))
    if num != 0:
        zad_1()
        print(num)


def zad_2(mess):
    if len(mess) <= 1:
        return True
    elif mess[0] != mess[-1]:
        return False
    else:
        return zad_2(mess[1:-1])


def zad_3(mess, ress=""):
    if len(mess) == len(ress):
        return ress
    else:
        ress = ress + mess[::-1]
        return zad_3(mess[::-1], ress)


def zad_4(mess):
    if len(mess) < 1:
        print(mess)
        return mess
    elif mess[0] == mess[-1]:
        return zad_4(mess[1:-1])
    else:
        return mess[0] + zad_4(mess[1:]) + mess[-1]


def zad_5(message):
    mess = list(message)
    res = ""
    for i in mess:
        if i == "'":
            res = res + '"'
        elif i == '"':
            res = res + "'"
        else:
            res = res + i
    return res


def zad_7(lst):
    if len(lst) <= 1:
        return None
    tup = []
    for i in range(len(lst) - 1):
        tup.append((lst[i], lst[i + 1]))
    return tup


def zad_8(str, lst):
    res = []
    index = 0
    for i in lst:
        if i > index and i < len(str):
            res.append(str[index:i])
            index = i
    res.append(str[index:])
    return res


def zad_9(lst):
    res = []
    a = 1
    for i in lst:
        for j in lst:
            if i != j:
                a = a * j
        res.append(a)
        a = 1
    print(res)
    return res
