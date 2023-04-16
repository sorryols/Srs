def calc(mess):
    li = list(mess.split(" "))
    a = float(li[0])
    b = float(li[2])
    op = li[1]

    chek_0 = False
    if b == 0:
        chek_0 = True
    if op == "+":
        print(f"Sum: {a+b}")
    if op == "-":
        print(f"Rizn: {a-b}")
    if op == "/" and chek_0 == True:
        print("[-]Error division by 0")
    if op == "/":
        print(f"Div: {a/b}")
    if op == "*":
        print(f"Mnoz: {a*b}")
    if op == "mod":
        print(f"Mod: {a%b}")
    if op =="pow":
        print(f"Pow: {pow(a,b)}")
    if op =="div":
        print(f"Div: {int(a/b)}")


def lucky_ticket(message):
    L = list(message)
    a1 = int(L[0])
    a2 = int(L[1])
    a3 = int(L[2])

    a4 = int(L[3])
    a5 = int(L[4])
    a6 = int(L[5])

    b1 = a1 + a2 + a3
    b2 = a4 + a5 + a6
    if b1==b2:
        print("Lucky")
    else:
        print("Unlucky")

def ferz():
    start = [4, 3]
    hod1 = [1, 1]
    if start[0] == hod1[0] or start[1] == hod1[1]:
        print("Yes")
    elif start[0]-hod1[0] == start[1]-hod1[1]:
        print("Yes")
    else:
        print("No")

def petro(n, m, x, y):
    if n>m:
        dist_1 = min(abs(n-y), y)
        dist_2 = min(abs(m-x), x)
    else:
        dist_1 = min(abs(m - y), y)
        dist_2 = min(abs(n - x), x)
    if dist_1 < dist_2:
        print(dist_1)
    else:
        print(dist_2)
