Roman_Conversions = {
    "I" :  1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    "IV" : 4,
    "IX" : 9,
    "XL" : 40,
    "XC" : 90,
    "CD" : 400,
    "CM" : 900
}

def RomanToInt(s):
    sum = 0
    n = len(s)
    i=0
    if n <=2:
        if s[i:i+2] in Roman_Conversions:
            return Roman_Conversions[s[i:i+2]]
        else:
            while i < n:
                sum = sum + Roman_Conversions[s[i]]
                i=i+1
            return sum
    else:
        while i<n:
            if i+1 < n and s[i:i+2] in Roman_Conversions:
                sum = sum + Roman_Conversions[s[i:i+2]]
                i = i +2
            else:
                sum = sum + Roman_Conversions[s[i]]
                i=i+1
        return sum
print(RomanToInt("MCMLXXVI"))


