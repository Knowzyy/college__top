n = int(input("введите размер стороны квадрата: "))

for i in range(n):
    a = ""
    for x in range(n):
        a += "*"
    print(a)
        
x = int(input("введите ширину прямоугольника: "))
y = int(input("введите высоту прямоугольника: "))
for i in range(x):
    a = ""
    for x in range(y):
        a += "*"
    print(a)
    
n = int(input("введите размер стороны квадрата: "))

for i in range(n):
    a = ""
    for x in range(n):
        if i == 0 or i == n - 1 or x == 0 or x == n - 1:
            a += "*"
        else:
            a +=" "
    print(a)
    
x = int(input("введите длину прямоугольника: "))
y = int(input("введите ширину прямоугольника: "))
for i in range(x):
    a = ""
    for j in range(y):
        if i == 0 or i == x - 1 or j == 0 or j == y - 1:
            a += "*"
        else:
            a += " "
    print(a)