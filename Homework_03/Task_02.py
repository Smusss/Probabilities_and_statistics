# Задача 2. 
# В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча. 
# Какова вероятность того, что 3 мяча белые?

import math as m

def quantity_of_combination(a: int, b: int):  # расчет количества сочетаний
    quantity = int(m.factorial(a) / (m.factorial(b) * m.factorial(a - b)))
    # print (quantity)
    return quantity


def probability(a: int, b: int):  # расчет условной вероятности
    chance = round(b / a, 5)
    return chance


all1 = 8
white1 = 5
take1 = 2

all2 = 12
white2 = 5
take2 = 4

max_white = 3

all_comb = quantity_of_combination(all1, take1) * quantity_of_combination(all2, take2)
good_comb = 0

for i in range(0, max_white):
    good_comb += quantity_of_combination(white1,i) * quantity_of_combination(white2,max_white - i)

result = probability(all_comb, good_comb)

print(f'Всего исходов: {all_comb}, благоприятных исходов: {good_comb}, вероятность {max_white} белых мячей исходя из условий: {result}.')

