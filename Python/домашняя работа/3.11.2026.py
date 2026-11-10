print("\nЗадание 1")
a = int(input("Введите число: "))
n = int(input("Введите число: "))

if a > n:
    a, n = n, a

sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0
sum_kr = 0
count_kr = 0

for i in range(a, n + 1):
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    else:
        sum_odd += i
        count_odd += 1

    if i % 9 == 0:
        sum_kr += i
        count_kr += 1

print(sum_even)
if count_even > 0:
    print(sum_even / count_even)

print(sum_odd)
if count_odd > 0:
    print(sum_odd / count_odd)

if count_kr > 0:
    print("Суммы кратных и среднее арифметическое 9", sum_kr, sum_kr / count_kr)
else:
    print("Не кратные 9")

print("\nЗадание 2")
len_l = int(input("введите длинну линии: "))
smale = input("введите символ для линии: ")
for _ in range(len_l):
    print(smale)