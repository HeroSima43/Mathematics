# Условие 1
# Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.

from math import sqrt

sigma = 16
m = 80
n = 256
Za2 = 1.96      # # Значение по таблице, по уровню значимости 0,025

x1 = m - Za2 * (sigma / sqrt(n))
x2 = m + Za2 * (sigma / sqrt(n))
print(f"Доверительный интервал: [{round(x1, 2)}; {round(x2, 2)}]")