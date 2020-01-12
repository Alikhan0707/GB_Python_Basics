seconds_from_user = int(input("Введите время в секундах: "))

hours = (seconds_from_user // 60) // 60
minutes = (seconds_from_user // 60) % 60
seconds = seconds_from_user % 60

print(f"{hours}:{minutes}:{seconds}")
