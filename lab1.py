import numpy as np
import matplotlib.pyplot as plt

# Создание случайной выборки
N = 20
sample = np.random.randint(1, 10, N)

# Вариационный ряд
variation_series = np.sort(sample)

# Гистограмма
plt.hist(sample, bins=10, edgecolor='black')
plt.title('Гистограмма')
plt.show()

# Полигон
plt.plot(variation_series, np.arange(1, N+1)/N, marker='o', linestyle='-')
plt.title('Полигон')
plt.show()

# Выборочное среднее
mean = np.mean(sample)

# Мода
mode = np.argmax(np.bincount(sample))

# Медиана
median = np.median(sample)

# Выборочная дисперсия
variance = np.var(sample)

# Стандартное отклонение
std_dev = np.std(sample)

# Коэффициент вариации
cv = std_dev / mean

# Размах
range_val = np.max(sample) - np.min(sample)

# Вывод результатов
print('Вариационный ряд:', variation_series)
print('Выборочное среднее:', mean)
print(f'Мода: {mode} occured {np.bincount(sample)[mode]} times')
print('Медиана:', median)
print('Выборочная дисперсия:', variance)
print('Стандартное отклонение:', std_dev)
print('Коэффициент вариации:', cv)
print('Размах:', range_val)
