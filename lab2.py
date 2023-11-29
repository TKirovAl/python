import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# данные
data = [52.2, 33, 76, 32.2, 49.5, 32.5, 191.5, 112.5, 32.9, 114.8, 33.7, 69.1, 112.5, 48.5, 16.5, 50, 51, 39, 66, 40, 70]

# вариационный ряд
var_series = pd.Series(data).sort_values()

# частотный ряд
freq_series = var_series.value_counts().sort_index()

# количество частичных интервалов
k = int(np.ceil(1 + 3.322 * np.log10(len(data))))

# интервальный ряд
interval_range = var_series.max() - var_series.min()
interval_width = interval_range / k
intervals = [round(var_series.min() + i * interval_width, 2) for i in range(k)]
intervals.append(var_series.max())  # добавляем последнюю границу
interval_counts, _ = np.histogram(var_series, bins=intervals)

# объединение пустых частичных интервалов с соседними
for i in range(k):
    if interval_counts[i] == 0:
        if i == 0:
            interval_counts[i+1] += 1
        elif i == k-1:
            interval_counts[i-1] += 1
        else:
            if interval_counts[i-1] > interval_counts[i+1]:
                interval_counts[i+1] += 1
            else:
                interval_counts[i-1] += 1

# середины интервалов
interval_midpoints = [(intervals[i] + intervals[i+1]) / 2 for i in range(len(intervals)-1)]

# дискретный вариационный ряд
discrete_var_series = pd.Series(interval_midpoints, index=interval_counts)

# построение полигона
plt.plot(discrete_var_series.index, discrete_var_series.values, marker='o')
plt.title('Полигон')
plt.xticks(rotation=45)
plt.show()

# построение частотного полигона
plt.bar(discrete_var_series.index, discrete_var_series.values, width=0.8)
plt.title('Частотный полигон')
plt.xticks(rotation=45)
plt.show()

# построение гистограммы
plt.bar(interval_midpoints, interval_counts, width=interval_width*0.8, edgecolor='black')
plt.title('Гистограмма')
plt.xticks(rotation=45)
plt.show()

# построение эмпирической функции распределения
ecdf = np.cumsum(discrete_var_series.values) / len(data)
plt.step(discrete_var_series.index, ecdf, where='post')
plt.title('Эмпирическая функция распределения')
plt.xticks(rotation=45)
plt.show()
