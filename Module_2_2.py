# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
# ***************************************************************************************
# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные
# first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else),
# которая выводит кол-во одинаковых чисел среди 3-х введённых.
#
# Пункты задачи:
#   - Если все числа равны между собой, то вывести 3
#   - Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
#   - Если равных чисел среди 3-х вообще нет, то вывести 0
# ****************************************************************************************

while True:
    try:
        first = int(input("Введите первое число >> "))
        break
    except:
        print()
        print("Повторите ввод без ошибок !")

while True:
    try:
        second = int(input("Введите второе число >> "))
        break
    except:
        print()
        print("Повторите ввод без ошибок !")

while True:
    try:
        third  = int(input("Введите третье число >> "))
        break
    except:
        print()
        print("Повторите ввод без ошибок !")


if first == second == third:
    print("Результат: 3")
elif first == second or first == third or second ==  third:
    print("Результат: 2")
else:
    print("Результат: 0")







