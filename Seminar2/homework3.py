# Условие 3.
# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def Bernoulli(n, k, p):
    return combination(n, k) * (p ** k) * ((1 - p) ** (n - k))


n = 144     # Число испытаний
k = 70      # Число наступления события
p = 0.5     # Вероятность наступления события в независимых испытаниях

print(f"Вероятность, что орел выпадет ровно 70 раз: {round(Bernoulli(n, k, p), 4)} или {round(Bernoulli(n, k, p) * 100, 2)} %")
