#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
'''

# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

def raise_power(_base, _exp):
    if _exp == 0:
        return 1
    elif _exp == 1:
        return _base
    elif _exp > 1:
        return _base * raise_power(_base, _exp - 1)
    elif _exp < 0:
        return 1 / raise_power(_base, _exp * (-1))

print("Программа запрашивает от пользователя два числа A и B")
print("Число А - это основание степени")
print("Число B - показатель степени")
print("На выходе программа показывает число A в степени B")
_a = int(input("Введите число A = "))
_b = int(input("Введите число B = "))
print(f'Число {_a} в степени {_b} = {raise_power(_a, _b)}')