# Задача 1.
# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
import math
import numpy as np


def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def average(list):  # среднее арифметическое
    sum = 0
    for i in list:
        sum += i
    avg = 1/len(list) * sum
    return avg


def standard_deviation(list):  # среднее квадратичное отклонение
    sum = 0
    for i in list:
        sum += i
    avg = 1/len(list) * sum
    sum = 0
    for i in list:
        sum += pow(i - avg, 2)
    sd_shifted = math.sqrt(sum / len(list))
    sd_non_shifted = math.sqrt(sum / (len(list) - 1))
    return sd_shifted, sd_non_shifted


def variance(list):
    sum = 0
    for i in list:
        sum += i
    avg = 1/len(list) * sum
    sum = 0
    for i in list:
        sum += pow(i - avg, 2)
    var_shifted = sum / len(list)
    var_non_shifted = sum / (len(list) - 1)
    return var_shifted, var_non_shifted


array = [100, 80, 75, 77, 89, 33, 45, 25, 65,
         17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

array_sum = sum(array)
array_avg = average(array)
array_sd_non_shifted = standard_deviation(array)[1]
array_var_shifted = variance(array)[0]
array_var_non_shifted = variance(array)[1]
print(f'Array: {array}.\nAverage: {round(array_avg,2)}.\n\
      Standart deviation: {round(array_sd_non_shifted,2)}.\n\
      Shifted varience: {round(array_var_shifted,2)}.\n\
      Non shifted variance: {round(array_sd_non_shifted,2)}')

# CHECK
a = np.mean(array)
b = np.std(array, ddof=1)
c = np.var(array, ddof=0)
d = np.var(array, ddof=1)
print(a)
print(b)
print(c)
print(d)
