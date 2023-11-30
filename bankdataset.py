import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('part_01.csv') #указываем путь к файлу
df1.head() #посмотрим несколько первых строк получившегося датафрейма
ptd1 = pd.read_csv('part_01.csv')
ptd2 = pd.read_csv('part_02.csv')
ptd3 = pd.read_csv('part_03.csv')
ptd4 = pd.read_csv('part_04.csv')
ptd5 = pd.read_csv('part_05.csv')
ptd6 = pd.read_csv('part_06.csv')
ptd7 = pd.read_csv('part_07.csv')
ptd8 = pd.read_csv('part_08.csv')
ptd9 = pd.read_csv('part_09.csv')
ptd10 = pd.read_csv('part_10.csv')
ptd11 = pd.read_csv('part_11.csv')
ptd12 = pd.read_csv('part_12.csv')

combined_dataset = pd.concat([ptd1, ptd2, ptd3, ptd4, ptd5, ptd6, ptd7, ptd8, ptd9, ptd10, ptd11, ptd12])

combined_dataset = combined_dataset.sort_values(by='ID')

combined_dataset = combined_dataset.drop_duplicates()

combined_dataset = combined_dataset.loc[:,~combined_dataset.columns.duplicated()]

print(combined_dataset.head(10))

print(f"Number of rows: {combined_dataset.shape[0]}, Number of columns: {combined_dataset.shape[1]}")

print("Duplicates in combined dataset:", combined_dataset.duplicated().any())
