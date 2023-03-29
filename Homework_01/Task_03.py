import math as m


def quantity_of_combination(a: int, b: int):  # расчет количества сочетаний
    quantity = int(m.factorial(a) / (m.factorial(b) * m.factorial(a - b)))
    # print (quantity)
    return quantity


def probability(a: int, b: int):  # расчет условной вероятности
    chance = round(b / a, 3)
    return chance

task = "\n***ЗАДАЧА 3***\nВ ящике имеется 15 деталей, из которых 9 окрашены.\n\
Рабочий случайным образом извлекает 3 детали.\n\
Какова вероятность того, что все 3 извлеченные детали окрашены?\n"

all_det = 15
coloured_det = 9
take = 3

take_in_all = quantity_of_combination(all_det, take)
take_in_coloured = quantity_of_combination(coloured_det, take)
result = probability(take_in_all,take_in_coloured)

# ОПИСАНИЕ РЕШЕНИЯ
print(task)
print(f"Для решения задачи найдем общее число сочетаний {take} деталей в наборе из {all_det}: {take_in_all}.\n\
Это число возможных исходов при извлечении заданного количества деталей.\n\
Количество сочетаний из {take}-х деталей в наборе окрашеных деталей ({coloured_det}): {take_in_coloured}.\n\
Это число благоприятных исходов при извлечении заданного количества деталей.\n\
Таким образом, чтобы расчитать вероятность того, что все {take} извлеченные детали - окрашеные,\n\
нужно разделить число благоприятных исходов ({take_in_coloured}) на общее число возможных исходов ({take_in_all}).\n\n\
ОТВЕТ ПО ЗАДАЧЕ: вероятность того, что все {take} извлеченные детали - окрашеные = {result}.\n\n")