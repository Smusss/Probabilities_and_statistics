# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
# Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), 
# а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.
import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

n = len(zp)
b1 = (n* np.sum(zp*ks) - np.sum(zp)*np.sum(ks)) / (n * np.sum(zp**2) - np.sum(zp)**2)
b0 = np.mean(ks) - b1 * np.mean(zp)
ks_pred = b0 + b1 * zp
mse = np.sum((ks - ks_pred)**2) / n
print(b0, b1, mse, ks_pred)






zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
sum_zp, sum_ks, sum_zp2, sum_zpks = 0, 0, 0, 0
for i in range(n):
    sum_zp += zp[i]
    sum_ks += ks[i]
    sum_zp2 += zp[i]**2
    sum_zpks += zp[i]*ks[i]

b1 = (n * sum_zpks - sum_zp*sum_ks) / (n * sum_zp2 - sum_zp**2)
b0 = sum_ks/n - b1 * sum_zp/n
ks_pred = []
sum_ks_pred2 = 0
for i in range(n):
    ks_pred.append(b0 + b1 * zp[i])
    sum_ks_pred2 += (ks[i] - ks_pred[i])**2
mse = sum_ks_pred2 / n
print(b0, b1, mse, ks_pred)




