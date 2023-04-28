# Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите: а). M(X)  б). D(X) в). std(X) (среднее квадратичное отклонение)
import math

x = 0
F = (1 / (4 * math.sqrt(2 * math.pi))) * math.exp((-(x + 2)**2) / 32)
#плотность вероятности подчиняется стандартной формуле, в соответствии с ней:

M = -2
s = 4
D = math.pow(s, 2)

print(f'M(x) = {M}, D(x) = {D}, std(x) = {s}.')