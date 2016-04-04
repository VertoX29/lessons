# Завдання: ввести два числа з консолі, вивести їх суму
print("Введіть два цілих числа, натисніть Enter для завершення; або просто Enter, щоб завершити")
total = 0
while True:
    line1 = input("Ціле число1: ")
    line2 = input("Ціле число2: ")
    if line1:
        try:
            number1 = int(line1)
        except ValueError as err:
            print(err)
            continue
    if line2:
        try:
            number2 = int(line2)
        except ValueError as err:
            print(err)
        total = number1 + number2
    else:
        break
    if total:
        print("Сумма введених чисел =", total)
        break