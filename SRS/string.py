def polinom(word):
    if len(word) % 2 == 1:
        a = int(len(word)/2)
        b = word[:a]
        ca = word[a+1::]
        ac = ca[::-1]
        if b == ac:
            return True
        else:
            return False
    else:
        a = int(len(word)/2)
        b = word[:a]
        ca = word[a::]
        ac = ca[::-1]
        if b == ac:
            return True
        else:
            return False

def swap_quotes(word):
    res = ""
    for i in word:
        if i == "'":
            res = res + '"'
        elif i == '"':
            res = res + "'"
        else:
            res = res + i
    return res

def get_longest_word(word):
    a = word.split()
    long = 0
    word = ""
    for i in a:
        if len(i) > long:
            long = len(i)
            word = i
    return word


