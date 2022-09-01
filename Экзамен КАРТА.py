# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
import random

card1 = [random.randint(0, 10) for i in range(16)]
print(len(card1))


def card():
    print(str('*' * (len(card1) - 4) + str(card1[-4:])))


card()
