x = int(input("Введите число от 1 до 100: "))
if x < 1 or x > 100:
    print("число не попадает в диапазон, ошибка!")
else:
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz Buzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


n = float(input("введите число"))  
s = int(input("введите степень (0–7): "))
if s < 0 or s > 7:
    print("разрешенный диапазон (0-7)")
else:
    if s == 0:
        num = 1
    else:
        num = x ** s
    print(num)
    
    
st = float(input("Введите стоимость минуты: "))
op = int(input("Выберите направление (1–6): "))
if op == 1:
    total = st * 2.0
elif op == 2:
    total = st * 2.1
elif op == 3:
    total = st * 2.2
elif op == 4:
    total = st * 2.3
elif op == 5:
    total = st * 2.5
elif op == 6:
    total = st * 2.6
else:
    print("направления не существует")
    total = 0 

if total != 0:
    print(total)