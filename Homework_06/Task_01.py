# 1. Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания с надежностью 0.95, 
# если выборочная средняя M = 80, а объем выборки n = 256.
import math
import scipy.stats as stats
s = 16

k = 0.95
M = 80
n = 256
alpha = 1 - k

interval_1 = M + stats.norm.ppf(alpha/2) * (s / math.sqrt(n))
interval_2= M - stats.norm.ppf(alpha/2) * (s / math.sqrt(n))

print(f'Доверительный интервал: ({interval_1}, {interval_2})')