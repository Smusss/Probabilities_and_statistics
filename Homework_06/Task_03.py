# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

import math
import numpy as np
import scipy.stats as stats


def work(array):
    prop = [0, 0, 0]
    prop[0] = np.mean(array)
    prop[1] = len(array)
    temp = 0
    for i in array:
        temp += pow(i - prop[0], 2)
    prop[2] = temp / (len(array)-1)
    return prop


def find_t(k, n1, n2):
    t = stats.t.ppf(k/2, df=n1+n2-2)
    return t


daughter = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
mother = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
k = 0.95

alpha = 1 - k
m_prop = work(daughter)
d_prop = work(mother)

M = m_prop[0] - d_prop[0]
D = 0.5 * (m_prop[2] + d_prop[2])
S = math.sqrt(D / m_prop[1] + D / d_prop[1])
t = find_t(alpha, m_prop[1], d_prop[1])

result_1 = M + t * S
result_2 = M - t * S

print(f'Доверительный интервал: ({result_1}, {result_2})')
