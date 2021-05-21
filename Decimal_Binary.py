def decimal(a):
    i = 0
    sum = 0
    while a != 0:
        rem = a % 10
        sum += rem * pow(2, i)
        i += 1
        a = a // 10
    return sum


print(decimal(11001))


def binary(num):
    d = num // 2
    rem = num % 2
    sum = rem
    while d != 1:
        rem = d % 2
        d = d // 2
        sum = (sum * 10) + rem
    sum = (sum * 10) + 1
    sum = str(sum)
    return sum[::-1]


print(binary(25))
