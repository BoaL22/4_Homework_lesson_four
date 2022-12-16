
from random import randint as rnd

def Dividers(a: int, uniq: bool = False) -> list[int]:
    i = 2
    dividers = []

    while a != 1:
        while a % i == 0:
            dividers.append(i)
            a //= i
        i += 1
    if uniq:
        return list(set(dividers))
    else:
        return dividers
    
a = 144
print(Dividers(a))
print(Dividers(a, True))
