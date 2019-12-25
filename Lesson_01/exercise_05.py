income = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издерки: "))

profit = income - costs

if profit > 0:

    print(f"Прибыль фирмы составляет: {profit}")

    profitability = profit / income

    number_of_employees = int(input("Введите число сотрудников: "))

    profit_per_employee = profit / number_of_employees

    print(f"Прибыль фирмы в расчете на одного сотрудника составляет: {profit_per_employee}")

elif profit < 0:

    print(f"Убыток фирмы составляет: {-profit}")

