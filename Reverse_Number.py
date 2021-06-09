def reverse_number(n):
    if n < 0:
        n = n * (-1)
        rev = 0
        while n > 0:
            rev = (rev * 10) + (n % 10)
            n = n // 10
        return -rev
    else:
        rev = 0
        while n > 0:
            rev = (rev * 10) + (n % 10)
            n = n // 10
        return rev


print(reverse_number(12345))
print(reverse_number(-12345))
print(reverse_number(10021))
print(reverse_number(11200))
