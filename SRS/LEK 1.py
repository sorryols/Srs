import math


def zad2(n, k):
    a = k / n
    a = int(a)
    zal = k - n * a
    print("Залишилось: " + str(zal) + " у кожного: " + str(a))


def zad3(xx, hh, mm):
    time_to_wake = hh * 60 + mm + xx
    H = int(time_to_wake / 60)
    M = time_to_wake - H * 60
    print("Hour: " + str(H) + " Minute: " + str(M))


def zad4(k1, k2, k3):
    all = k1 + k2 + k3
    part = all / 2
    if part - int(part) != 0:
        part = int(part) + 1
    else:
        part = int(part)
    print("Part: " + str(part))


def zad5():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    c = int(input("Введіть третє число: "))

    max_num = (a + b + abs(a - b)) / 2
    max_num = (max_num + c + abs(max_num - c)) / 2

    min_num = (a + b - abs(a - b)) / 2
    min_num = (min_num + c - abs(min_num - c)) / 2

    mid_num = (a + b + c) - max_num - min_num

    print(str(int(max_num)) + "\t" + str(int(min_num)) + "\t" + str(int(mid_num)))


def zad_shnurok(a, b, l, N):
    a1 = int(N / 4)

    res = (N * a) + 2 * (b * (N - a1 - 1)) + l
    print("Result: " + str(res) + "sm")
