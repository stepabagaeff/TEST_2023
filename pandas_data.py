import pandas as pd



str_d = '\n' + '-'  * 100 # Разделительная строка

# Задания:

# 1.	Импортируйте библиотеку Pandas и прочитайте данные из файла "data.csv" в DataFrame.

df = pd.read_csv('data.csv', delimiter=',')
print('1.	Импортируйте библиотеку Pandas и прочитайте данные из файла "data.csv" в DataFrame.\n')
print(df, str_d)

# 2.	Выведите первые 3 строки DataFrame.

first_rows = df.head(3)
print('2.	Выведите первые 3 строки DataFrame.\n')
print(first_rows, str_d)

# 3.	Посчитайте общее количество записей в DataFrame.

count_rows = len(df.index)
print('3.	Посчитайте общее количество записей в DataFrame.\n')
print(f'Общее количество записей: {count_rows}', str_d)

# 4.	Выведите все строки, где значение в столбце "age" больше 17.

over_17 = df[df.age > 17]
print('4.	Выведите все строки, где значение в столбце "age" больше 17.\n')
print(over_17, str_d)

# 5.	Сгруппируйте данные по столбцу "gender" и посчитайте средний возраст для каждой группы.

gp_gender = df.groupby('gender')['age'].mean()
print('5.	Сгруппируйте данные по столбцу "gender" и посчитайте средний возраст для каждой группы.\n')
print(gp_gender)
