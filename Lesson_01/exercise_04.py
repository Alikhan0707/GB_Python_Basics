number = int(input("Введите любое число: "))

i = 1
k = 1  # Степень 10
d = 0  # Наибольшая цифра
n = number  # Чило меньшее number на 10 в степени k

while i <= number:

    if i > 10:
        k += 1

    i *= 10

while k >= 0:

    kn = n // (10 ** k)

    n -= kn * (10 ** k)

    if kn > d:

        d = kn

    k -= 1

print(d)