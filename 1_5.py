proceeds = int(input("Введите значение выручки предприятия "))
costs = int(input("Введите значение издержек предприятия "))
profit = proceeds - costs
rent = profit / proceeds * 100
if proceeds > costs:
    print("Предприятие рентабельно! Прибыль составила ", profit)
    print(f"Рентабельность составила {rent:.2f} %")
    employees = int(input("введите численность работников"))
    prof_emp = int(profit / employees)
    print(f"Прибыль на 1 сотрудника составила:  {rent:.2f}")
else:
    print('При всем уважении, но дальнейший расчет не имеет смысла. убыток составил: ', profit)