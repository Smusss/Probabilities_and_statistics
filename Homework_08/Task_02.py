# Задача 2 Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import math as m
import numpy as np
import scipy.stats as stats

iq = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
p = 0.95

alpha = 1 - p
M = np.mean(iq)
# s = m.sqrt(np.var(iq,ddof=1))
s = np.std(iq, ddof=1)
interval_1 = M + stats.t.ppf(alpha/2, df=len(iq)-1) * (s / m.sqrt(len(iq))) # норм распр, дисп ГС НЕ известна => t
interval_2 = M - stats.t.ppf(alpha/2, df=len(iq)-1) * (s / m.sqrt(len(iq)))

print(f'Доверительный интервал: ({interval_1}, {interval_2})')
