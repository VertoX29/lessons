print("Введіть два цілих числа, натисніть Enter для завершення; або просто Enter, щоб завершити")
total = 0
x = input("Введіть х: ")
y = input("Введіть y: ")
def input_init(x, y):
    if x != int(x):
        print("Ви ввели невірне значення!")
    elif x == None:
        exit()
    if y != int(y):
        print("Ви ввели невірне значення!")
input_init(x, y)