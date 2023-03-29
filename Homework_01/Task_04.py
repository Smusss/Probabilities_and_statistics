import math as m


def quantity_of_combination(a: int, b: int):  # расчет количества сочетаний
    quantity = int(m.factorial(a) / (m.factorial(b) * m.factorial(a - b)))
    # print (quantity)
    return quantity


def probability(a: int, b: int):  # расчет условной вероятности
    chance = round(b / a, 5)
    return chance


task = "\n***ЗАДАЧА 4***\nВ лотерее 100 билетов. Из них 2 выигрышных.\n\
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?\n"

all = 100 # всего элементы
win = 2 # из них нужные
take = 2 # сколько изымаем
point = 2 # сколько нужных хотим получить, минимум. Но не более количества нужных
combination_with_win = 0

take_in_all = quantity_of_combination(all, take) # все сочетания при покупке N билетов

for i in range(point, win + 1):
    combination_with_win += quantity_of_combination(all - win, take - i) * quantity_of_combination(win, i)

chance_to_take_point = probability(take_in_all, combination_with_win)

# ОПИСАНИЕ РЕШЕНИЯ
print(task)
print(f"Для решения задачи найдем общее число сочетаний {take} билетов в наборе из {all}: {take_in_all}.\n\
Это число возможных исходов при покупке заданного количества билетов.\n\
Количество сочетаний из {take} билетов в количестве выйгрышных билетов ({win}): {combination_with_win}.\n\
Это число благоприятных исходов при покупке заданного количества билетов.\n\
Таким образом, чтобы расчитать вероятность того, что минимум {take} купленных билета - выйгрышные,\n\
нужно разделить число благоприятных исходов ({combination_with_win}) на общее число возможных исходов ({take_in_all}).\n\n\
ОТВЕТ ПО ЗАДАЧЕ: вероятность того, что минимум {point} билета из {take} выйгрышные  = {chance_to_take_point}.\n\n")