# Условие 2.
# Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).

import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


def mse(b1, x, y, n):
    return np.sum((y - b1 * x)**2) / n


n = 10
alpha = 0.000001
b1 = 0.1

for i in range(1001):
    b1 -= alpha * (2 / n) * np.sum((b1 * zp - ks) * zp)
    if i % 100 == 0:
        print(f"Iteranion = {i}, b1 = {b1}, mse = {mse(b1, zp, ks, n)}")
