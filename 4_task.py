
with open('numbers.txt', 'r') as file:
    list = [(int(i), int(i)**2) for i in file if int(i) % 2 == 0]

    print(list)

