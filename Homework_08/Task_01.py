# Задача 1 Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

import numpy as np
import math as m

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

# ручной расчет среднее - ковариация - сигма - коэф.корреляции
sum_zp, sum_ks, sum_zpks = 0, 0, 0
for i in range(len(zp)):
    sum_zp = sum_zp + zp[i]
    sum_ks = sum_ks + ks[i]
    sum_zpks = sum_zpks + zp[i]*ks[i]
M_zp = sum_zp / len(zp)
M_ks = sum_ks / len(ks)
M_zpks = sum_zpks / len(zp)

cov = M_zpks - M_zp*M_ks # смещ

temp_zp, temp_ks = 0, 0
for i in range(len(zp)):
    temp_zp += pow(zp[i] - M_zp, 2)
    temp_ks += pow(ks[i] - M_ks, 2)

S_zp = m.sqrt(temp_zp / (len(zp))) # смещ
S_ks = m.sqrt(temp_ks / (len(ks))) # смещ

r_zpks = cov / (S_zp * S_ks)
print(f'ручной расчет: {r_zpks}.')

# полуручной расчет ковариация - сигма - коэф.корреляции (не смещ)
zpks = []
for i in range(len(zp)):
    zpks.append(zp[i] * ks[i])
#cov = np.mean(zpks) - np.mean(zp)*np.mean(ks) # смещ
cov = np.cov(zp, ks,ddof = 1)   # не смещ
szp = m.sqrt(np.var(zp, ddof=1)) # не смещ
sks = m.sqrt(np.var(ks, ddof=1)) # не смещ
r_zpks = cov / (szp * sks)
print(f'полуручной расчет: \n {r_zpks}.')

# проверка. смещенная
r_zpks = np.corrcoef(zp,ks)
print(f'проверка автом.расчет: \n {r_zpks}.') # не смещ