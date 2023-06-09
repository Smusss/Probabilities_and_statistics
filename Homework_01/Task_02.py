import math as m


def quantity_of_combination(a: int, b: int):  # расчет количества сочетаний
    quantity = int(m.factorial(a) / (m.factorial(b) * m.factorial(a - b)))
    # print (quantity)
    return quantity


def probability(a: int, b: int):  # расчет условной вероятности
    chance = round(b / a, 3)
    return chance

task = "\n***ЗАДАЧА 2***\nНа входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.\n\
Код содержит три цифры, которые нужно нажать одновременно.\n\
Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?\n"

numbers = 10
code = 3
turn = 1
all_codes = quantity_of_combination(numbers, code)
probability_of_right_code = probability(all_codes, turn)

# ОПИСАНИЕ РЕШЕНИЯ
print(task)
print(f"Для решения задачи необходимо расчитать сколько вариантов кода из {code} цифр можно составить на замке,\n\
содержащем {numbers} цифр. Так как цифры нажимаются одновременно, порядок нам не важен, соответственно ищем количество сочетаний.\n\
Это число возможных исходов. Так как открыть нужно с первой попытки, число благоприятных исходов = {turn}.\n\
Таким образом, чтобы расчитать вероятность того, что человек с {turn} попытки введет код из {code} цифр на замке,\n\
содержащем {numbers} цифр (при этом цифры кода вводятся одновременно), нужно разделить число благоприятных исходов ({turn}) \n\
а общее число возможных исходов ({all_codes}).\n\n\
ОТВЕТ ПО ЗАДАЧЕ: вероятность того, что код введен верно = {probability_of_right_code}. \n\n")