def roman_to_int(num):
    Roman_Conversions = {"I": 1,
                         "V": 5,
                         "X": 10,
                         "L": 50,
                         "C": 100,
                         "D": 500,
                         "M": 1000,
                         "IV": 4,
                         "IX": 9,
                         "XL": 40,
                         "XC": 90,
                         "CD": 400,
                         "CM": 900
                         }
    i = 0
    sums = 0
    while i < len(num):
        if num[i: i + 2] in Roman_Conversions:
            sums += Roman_Conversions[num[i: i + 2]]
            i += 2
        elif num[i] in Roman_Conversions:
            sums += Roman_Conversions[num[i]]
            i += 1
    return sums


print(roman_to_int("MCMLXXVI"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))
