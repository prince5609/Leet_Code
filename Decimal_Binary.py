def decimal(a):
    i = 0
    sums = 0
    while a != 0:
        rem = a % 10
        sums += rem * pow(2, i)
        i += 1
        a = a // 10
    return sums


print(decimal(11001))


def binary(num):
    d = num // 2
    rem = num % 2
    sums = rem
    while d != 1:
        rem = d % 2
        d = d // 2
        sums = (sums * 10) + rem
    sums = (sums * 10) + 1
    sums = str(sums)
    return sums[::-1]


print(binary(25))
