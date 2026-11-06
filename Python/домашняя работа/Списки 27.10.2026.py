print("\nЗадание 1")
import random
list1 = []
for i in range(10):
    num = random.randint(-5, 5)
    list1.append(num)

print(list1)
"""сумма отрицательного числа"""
summa = 0
for j in list1:
    if j < 0:
        summa += j
        
print(summa)
"""сумма четного числа"""
summa1 = 0
for j in list1:
    if j % 2 == 0:
        summa1 += j
        
print(summa1)
"""сумма нечетного числа"""
summa2 = 0
for j in list1:
    if j % 2 != 0:
        summa2 += j
        
print(summa2)
"""произведение элементов с индаксами кратные 3"""
index1 = 1
for i in list1[0::3]:
    index1 *= i
print(index1)
"""произведение элементов можду мин и макс элементом"""
min1 = list1.index(min(list1))
max1 = list1.index(max(list1))
start = min(min1, max1) + 1
end = max(min1, max1)

total = 1
if start < end:
    for i in range(start, end):
        total *= list1[i]
else:
    total = 0
print(total)
"""сумма элементов между первым и 
последним положительными элементами
"""
pl_index = []
for i in range(len(list1)):
    x = list1[i]
    if x > 0:
        pl_index.append(i)

summa_pl = 0
if len(pl_index) >= 2:
    pl1 = pl_index[0]
    pl2 = pl_index[-1]
    for i in range(pl1 + 1, pl2):
        summa_pl += list1[i]
        
print(summa_pl)
        
print("\nЗадание 2")
even_list1 = []
odd_list1 = []
neg_list1 = []
pos_list1 = []
for j in list1:
    if j % 2 == 0:
        even_list1.append(j)
    else:
        odd_list1.append(j)   
    if j < 0:
        neg_list1
    else:
        pos_list1.append(j)

print(even_list1)
print(odd_list1)
print(neg_list1)
print( pos_list1)