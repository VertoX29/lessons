#Функція повинна мати один параметр (текст підказки користувачеві),
#  підказка виводитиметься, доки користувач не введе ціле
# число або порожній рядок. Функція повертає ціле число
# (якщо воно було введене) або None (якщо нічого введено не було)
def input_int(pidkazka):
    while True:
        print(pidkazka)
        line=input()
        if line=='':
            return None
        try:
            return int(line)
        except:
            continue

if __name__=='__main__':
    x=input_int('Введіть x')
    if x==None:
        exit()
    y=input_int('Введіть y')
    if y==None:
        exit()
    print('x*y', x*y)
