# Напишите функцию, которая проверяет: является ли слово палиндромом


def slovo(a):
    return a[::-1]


def slovo1(a):
    b = slovo(a)

    if a == b:
        return True
    else:
        return False


a = input('Введите слово палинтроп: ')
c = slovo1(a)
print(c)
