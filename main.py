# 1. Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит на экран максимум из трёх
# минимум из трёх или среднеарифметическое трёх чисел.

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second num: "))
third_num = int(input("Enter third num: "))

chose_operation = int(input("Please chose operation:\n1)Max of 3-digit\n2)Min of 3-digit\n3)Simple average"))

if chose_operation == 1:
    maximum = max(first_num, second_num, third_num)
    print(maximum)
elif chose_operation == 2:
    minimum = min(first_num, second_num, third_num)
    print(minimum)
else:
    simple_average = (first_num + second_num + third_num) / 3
    print(simple_average)
