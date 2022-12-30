
# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$ / $10^{-1} ≤ d ≤10^{-10}$ 3,1415926535

from math import pi
with open('accuracy.txt', 'r', encoding='utf-8') as file:
    d = float(file.readline())
i = 0
while d < 1:
    d = d * 10
    i += 1
print(f'π = {str(pi)[:i+2]}') # сокращение 3.141592
print(f'π = {round(pi, i)}') # окпугление  3.141593

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число N: '))
i = 2
arr = []
while (i <= N):
    if N % i == 0:
        arr.append(i)
        N = N/i
    else:
        i += 1
print(arr) # input 30 = 2,3,5

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

with open('array_task3.txt', 'r', encoding='utf-8') as file:
    listA = file.readline()
listB = []
for el in listA:
    if listA.count(el) == 1:
        listB.append(el)
print(*listB)  # [2, 4, 5, 2, 2, 4, 6, 7, 8, 9, 6] ==>> [ 5 7 8 9 ]