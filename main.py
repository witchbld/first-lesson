# 1. Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит на экран максимум из трёх
# минимум из трёх или среднеарифметическое трёх чисел.

# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second num: "))
# third_num = int(input("Enter third num: "))
#
# chose_operation = int(input("Please chose operation:\n1)Max of 3-digit\n2)Min of 3-digit\n3)Simple average"))
#
# if chose_operation == 1:
#     maximum = max(first_num, second_num, third_num)
#     print(maximum)
# elif chose_operation == 2:
#     minimum = min(first_num, second_num, third_num)
#     print(minimum)
# else:
#     simple_average = (first_num + second_num + third_num) / 3
#     print(simple_average)

print("_____second task_____")

# 2. Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды.

user_input_meters = int(input("Enter the number of metres to be converted to another unit: "))

chose_operation = int(input("Please chose operation:\n1)Convert to miles\n2)Convert to inch\n3)Convert to yards"))

if chose_operation == 1:
    miles = user_input_meters * 0.000621371
    print(f"{miles} miles in {user_input_meters} meters.")
elif chose_operation == 2:
    inch = user_input_meters * 39.37
    print(f"{inch} inches in {user_input_meters} meters.")
else:
    yards = user_input_meters * 1.094
    print(f"{yards} yards in {user_input_meters} meters.")
