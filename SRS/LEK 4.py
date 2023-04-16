from typing import Tuple, Any


def zad_1(message):
    mess = list(message)
    res = ""
    for i in mess:
        if i == "'":
            res = res + '"'
        elif i == '"':
            res = res + "'"
        else:
            res = res + i
    print(res)


def zad_2(message):
    if not isinstance(message, str):
        print("[-]Error incorect value")
        return False

    message = message.replace(" ", "").lower()

    if len(message) < 2:
        return False

    for i in range(len(message) // 2):
        if message[i] != message[-i - 1]:
            return False
    return True


def zad_3(message, delim=None):
    result = []
    word = ""

    if not isinstance(message, str):
        print("[-]Error incorect value")
        return ""
    if delim is None:
        delim = " "

    for i in message:
        if i == delim:
            result.append(word)
            word = ""
        else:
            word = word + i
    result.append(word)

    return result


def zad_5(*args: int) -> tuple[int | Any, ...]:
    digits = []
    for i in args:
        arg_digits = []
        while i > 0:
            digit = i % 10
            arg_digits.append(digit)
            i = i // 10
        digits.extend(reversed(arg_digits))
    return tuple(digits)

def zad_6(message):
    mes = zad_3(message)
    word = ""
    long = 0
    for i in mes:
        if len(i) > long:
            word = i
            long = len(i)

    return word

def zad_7(list):
    res = []
    to_add = 1
    for i in list:
        for j in list:
            if j !=i:
                to_add = to_add * j
        res.append(to_add)
        to_add = 1
    return res

def zad_8(lst):
    res = []
    chunk = []
    col = 1
    n = 2
    if len(lst) < 2:
        return None

    for i in range(0, len(lst)):
        chunk.append(lst[i])
        if col == n:
            res.append(chunk)
            chunk = []
            col = 0

        col = col + 1
    if len(chunk) != 0:
        res.append(chunk)
    return res

def zad_9(number):
    res = 0

    if not isinstance(number, int):
        print("[-]Error incorect value")
        return None

    while number > 0:
        digit = number % 10

        if digit % 2 == 1:
            res = res + digit

        number //= 10
    return res

def zad_10(n):
    binary = bin(n)[2:]
    col = 0

    lst = list(binary)
    for i in lst:
        if i == '1':
            col = col + 1
    return col