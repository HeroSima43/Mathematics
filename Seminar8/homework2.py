# Условие 2.
# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

from math import sqrt
from numpy import mean, std
import scipy.stats as stats

sample = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
Ta2 = stats.t.ppf(0.975, 9)

x1 = mean(sample) - Ta2 * (std(sample, ddof=1) / sqrt(len(sample)))
x2 = mean(sample) + Ta2 * (std(sample, ddof=1) / sqrt(len(sample)))
print(f"Доверительный интервал: [{round(x1, 2)}; {round(x2, 2)}]")
