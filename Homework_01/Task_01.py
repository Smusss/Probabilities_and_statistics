import math as m


def quantity_of_combination(a: int, b: int):  # расчет количества сочетаний
    quantity = int(m.factorial(a) / (m.factorial(b) * m.factorial(a - b)))
    # print (quantity)
    return quantity


def probability(a: int, b: int):  # расчет условной вероятности
    chance = round(b / a, 3)
    return chance


task = "\n***ЗАДАЧА 1***\nИз колоды в 52 карты извлекаются случайным образом 4 карты.\n\
a) Найти вероятность того, что все карты – крести.\n\
б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.\n"

all = 52  # всего карт
clubs = int(all/4)  # крести 1\4 колоды
aces = 4  # тузы в колоде
take = 4  # количество выбираемых карт
ace_in_hand = 1  # минимальное количество тузов в выборке

take_in_all = quantity_of_combination(all, take)  # сочетания 4 в 52
take_in_clubs = quantity_of_combination(clubs, take)  # сочетания 4 в крести
chance_clubs = probability(take_in_all, take_in_clubs)  # вероятность крести

combination_with_aces = 0
for i in range(ace_in_hand, aces + 1):
    combination_with_aces += quantity_of_combination(all - aces, take - i) * quantity_of_combination(aces, i)
chance_aces = probability(take_in_all, combination_with_aces)

print(combination_with_aces)
print(chance_aces)


# ОПИСАНИЕ РЕШЕНИЯ
print(task)
print(f"Для решения обеих подзадач найдем общее число сочетаний {take} карт в колоде из {all}: {take_in_all}.\n\
Это число возможных исходов при извлечении заданного количества карт.\nПУНКТ А:\n\
Количество карт масти крести в колоде = {all} / 4 = {clubs}.\n\
Количество сочетаний из {take}-х разных карт масти крести в общем количестве карт этой масти ({clubs}): {take_in_clubs}.\n\
Это число благоприятных исходов при извлечении заданного количества карт.\n\
Таким образом, чтобы расчитать вероятность того, что все {take} извлеченные карты - крести,\n\
нужно разделить число благоприятных исходов ({take_in_clubs}) на общее число возможных исходов ({take_in_all}).\n\n\
ОТВЕТ ПО ПУНКТУ А: вероятность того, что все {take} карты извлеченные карты - крести = {chance_clubs}.\n\n\
ПУНКТ Б:\nКоличество тузов в колоде = {aces}.\n\
Извлекаются {take} карты, минимум {ace_in_hand} из них по условиям задачи должна быть тузом (возможно и более).\n\
Количество сочетаний {ace_in_hand} и более тузов с остальными картами колоды (колода минус тузы) можно посчитать из логики:\n\
количество сочетаний N тузов из {aces} и/* сочетаний остатка извлеченных карт ({take} - N) в колоде без тузов.\n\
Перемножив количество сочетаний тузов и оставшихся на руках карт (И), \n\
получаем количество благоприятных исходов = {combination_with_aces}.\n\n\
Таким образом, чтобы расчитать вероятность того, что среди {take} извлеченных карт будет хотя бы {ace_in_hand} туз,\n\
нужно разделить число благоприятных исходов ({combination_with_aces}) на общее число возможных исходов ({take_in_all}).\n\n\
ОТВЕТ ПО ПУНКТУ Б: вероятность того, что среди {take} извлеченных карт будет хотя бы {ace_in_hand} туз = {chance_aces}.\n")


# ace_in_aces = quantity_of_combination(aces, ace_in_hand)  # сочетания 1 в 4 тузах
# take_without_ace_in_all_without_aces = quantity_of_combination(all - aces, take - ace_in_hand)  # сочетания 3х оставшихся на руках картах в колоде без тузов
# chance_ace = probability(take_in_52, take_without_ace_in_all_without_aces*ace_in_aces) # вероятность что 1 из 4 туз