# Условие 1.
# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

from numpy import cov, corrcoef
from math import sqrt
import matplotlib.pyplot as plt

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]


def average(list):
    sum = 0
    for i in list:
        sum = sum + i
    avr = sum / len(list)
    return avr


def multi_list(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] * list2[i])
    return list3


cov_r = average(multi_list(zp, ks)) - average(zp) * average(ks)
print(f"Расчетное значение ковариации: {round(cov_r, 2)}")
print(f"Проверка: {cov(zp, ks, ddof=0)}")


def sum_of_squared_deviations(list):        # Рассчитаем сумму квадратов отклонений значений относительно среднего
    sum = 0
    for i in list:
        sum = sum + (i - average(list)) ** 2
    return sum


sdo_zp = sqrt(sum_of_squared_deviations(zp) / len(zp))
sdo_ks = sqrt(sum_of_squared_deviations(ks) / len(ks))

r = cov_r / (sdo_zp * sdo_ks)
print(f"Расчетное значение коэффициента корреляции: {round(r, 4)}")
print(f"Проверка: {corrcoef(zp, ks)}")

plt.scatter(zp, ks)
plt.title(f"Коэффициент корреляции: {round(r, 4)}")
plt.xlabel(zp)
plt.ylabel(ks)
plt.show()
