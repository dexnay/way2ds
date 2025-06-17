# ѕолучаем количество €блок из ввода
total_apples = int(input("¬ведите количество купленных €блок: "))

# ƒелим €блоки поровну между 4 членами семьи
apples_per_person = total_apples // 4  # целочисленное деление
total_for_trip = apples_per_person * 4  # общее количество €блок дл€ похода
apples_to_leave = total_apples % 4      # остаток €блок

# ¬ыводим результаты
print(f"¬сего куплено €блок: {total_apples}")
print(f"Ќа каждого члена семьи приходитс€: {apples_per_person} €блок")
print(f"Ќужно вз€ть в поход: {total_for_trip} €блок")
print(f"Ќужно оставить дома: {apples_to_leave} €блок")
