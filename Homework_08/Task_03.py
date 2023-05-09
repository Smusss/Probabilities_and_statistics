# Задача 3 Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см. 
# Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import math as m
import numpy as np
import scipy.stats as stats

D = 25
n = 27
M = 174.2
p = 0.95

alpha = 1 - p
s = m.sqrt(D)

interval_1 = M + stats.norm.ppf(alpha/2) * (s / m.sqrt(n)) # норм распр, дисп ГС известна => Z
interval_2 = M - stats.norm.ppf(alpha/2) * (s / m.sqrt(n))

print(f'Доверительный интервал: ({interval_1}, {interval_2})')