def f(m,n):
    i = m
    res = 1
    while i <= n:
        res *= i
        i += 1
    return res
print('Загальний добуток: ', f(3, 13))
