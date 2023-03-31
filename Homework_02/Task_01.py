import math as m


def quantity_of_combination(a: int, b: int):  # расчет количества сочетаний
    quantity = int(m.factorial(a) / (m.factorial(b) * m.factorial(a - b)))
    return quantity


def probability(a: int, b: int):  # расчет условной вероятности
    chance = round(b / a, 3)
    return chance


def bernulli(n: int, k: int, p: float):
    q = 1-p
    probability_bern = round((m.factorial(
        n) / (m.factorial(k) * m.factorial(n - k))) * m.pow(p, k) * m.pow(q, n - k), 4)
    return probability_bern


def puasson(l, w):
    probability_pu = round((m.pow(l, w) / m.factorial(w)) * m.pow(m.e, -l), 4)
    return probability_pu


task = '\n1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.\n\
Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.'

p = 0.8
n = 100
k = 85

result_task = bernulli(n, k, p)

print(task)
print('Распределение биноминальное, вероятность большая, испытаний условно не много, используем формулу Бернулли.')
print(f'Ответ по задаче 1: {result_task}')

task = '\n2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.\n\
В жилом комплексе после ремонта в один день включили 5000 новых лампочек.\n\
Какова вероятность, что ни одна из них не перегорит в первый день?\n'

p = 0.0004
n = 5000
w = 0

l = n * p
result_task = puasson(l, w)

print(task)
print('Распределение биноминальное, вероятность маленькая, испытаний много - распределение Пуассона.')
print(
    f'Ответ по задаче 2.1: {result_task} (вероятность, что ни одна из них не перегорит в первый день)')

task = 'Какова вероятность, что перегорят ровно две?'

w = 2
l = n * p
result_task = puasson(l, w)

print(
    f'Ответ по задаче 2.2: {result_task} (вероятность, что перегорят ровно две)')


task = '\n3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?'

p = 0.5
n = 144
k = 70

result_task = bernulli(n, k, p)

print(task)
print('Распределение биноминальное, вероятность большая, испытаний условно не много, используем формулу Бернулли.')
print(f'Ответ по задаче 3: {result_task}')


task = '\n4. В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.\n\
Из каждого ящика вытаскивают случайным образом по два мяча.\n\
Какова вероятность того, что все мячи белые?\n'
all1 = 10
all2 = 11
white1 = 7
white2 = 9
take = 2

all_combination = quantity_of_combination(
    all1, take) * quantity_of_combination(all2, take)

good_combination = quantity_of_combination(
    white1, take) * quantity_of_combination(white2, take)
result_task = probability(all_combination, good_combination)
print(f'{task}Ответ по задаче 4.1: {result_task}.\n\n\
Какова вероятность того, что ровно два мяча белые?')

'''
good_combination = quantity_of_combination(white1, take)*quantity_of_combination(all2 - white2, take) + quantity_of_combination(
    white2, take) * quantity_of_combination(all1 - white1,  take) + quantity_of_combination(white1, int(take / 2)) * quantity_of_combination(white2, int(take / 2))
result_task = probability(all_combination, good_combination)
print(f'Ответ по задаче 4.2: {result_task}.\n\n\
'''

print('Какова вероятность того, что хотя бы один мяч белый?')

bad_combination = quantity_of_combination(all1 - white1, take) * quantity_of_combination(all2 - white2, take) #варианты когда все - не белые
good_combination = all_combination - bad_combination
result_task = probability(all_combination, good_combination)
print(f'Ответ по задаче 4.3: {result_task}.')