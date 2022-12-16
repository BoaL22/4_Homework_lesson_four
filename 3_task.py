    # Задача №32: Задайте последовательность чисел. 
    # Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = list(map(int, input("Введите числа через пробел:\n").split()))
list_2 = []

for number in list:
    if number not in list_2:
        list_2.append(number)

print(list)
print(list_2)