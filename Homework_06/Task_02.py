#  В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95.
import math
import numpy as np
import scipy.stats as stats

array_x = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
k = 0.95
alpha = 1 - k

M = np.mean(array_x)
n = len(array_x)
temp = 0
for i in array_x:
    temp += pow(i - M, 2)
s = math.sqrt(temp / (n-1))

interval_1 = M + stats.t.ppf(alpha/2, df=n-1) * (s / math.sqrt(n))
interval_2 = M - stats.t.ppf(alpha/2, df=n-1) * (s / math.sqrt(n))

print(f'Доверительный интервал: ({interval_1}, {interval_2})')
