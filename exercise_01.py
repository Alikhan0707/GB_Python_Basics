name = input("Введите имя: ")
age = int(input("Введите возраст: "))
country = input("Введите страну: ")

if age % 5 == 0:
    print(f"Меня зовут {name}, мне {age} лет, я из {country}")
elif age % 5 > 0 and (age // 5) % 2 == 0:
    print(f"Меня зовут {name}, мне {age} год(а), я из {country}")

