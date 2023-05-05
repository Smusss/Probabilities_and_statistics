#  Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
import math

a = 200
b = 800

M = (b - a) / 2
D = math.pow(b - a, 2) / 12
s = math.sqrt(D)

print(f'Среднее значение = {M}, дисперсия = {D}.')