import random
list1 = [random.randint(0, 200) for _ in range(10)]
list2 = [random.randint(0, 200) for _ in range(10)]
print(list1, list2)

list3 = list1 + list2
print(list3)

no_elements = []
for i in list3:
    if i not in no_elements:
        no_elements.append(i)
print(no_elements)

num = []
for i in list1:
    if i in list2 and i not in num:
        num.append(i)
print(num)

epic = []
for i in no_elements:
    a = i in list1
    b = i in list2
    if a != b:
        epic.append(i)   
print(epic)

min_max_list = [min(list1), max(list1), min(list2), max(list2)]
print(min_max_list)