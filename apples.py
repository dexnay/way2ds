# Получаем количество яблок из ввода
total_apples = int(input("Введите количество купленных яблок: "))

# Делим яблоки поровну между 4 членами семьи
apples_per_person = total_apples // 4  # целочисленное деление
total_for_trip = apples_per_person * 4  # общее количество яблок для похода
apples_to_leave = total_apples % 4      # остаток яблок

# Выводим результаты
print(f"Всего куплено яблок: {total_apples}")
print(f"На каждого члена семьи приходится: {apples_per_person} яблок")
print(f"Нужно взять в поход: {total_for_trip} яблок")
print(f"Нужно оставить дома: {apples_to_leave} яблок")
