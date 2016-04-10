def f(m,n):
    i = m
    res = 0
    while i <= n:
        res += i
        i += 1
    return res
print('Загальна сумма: ', f(3, 13))
