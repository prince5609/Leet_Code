# REVERSE AN ARRAY

def reverse(array):
    n = len(array)
    m = n // 2
    for i in range(m):
        temp = array[i]
        array[i] = array[n - i - 1]
        array[n - i - 1] = temp
    return array


print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(reverse([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
