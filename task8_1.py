# Написати функцію, що в діапазоні чисел від m до n
# знаходить найменше ціле число, що ділиться без остачі на k
# m, n, k — параметри функції.
# m = 10, n = 30, k = 7
def numbers(m, n, k):
    i = m
    while i >= m:
        if i % k == 0:
            return(i)
        else:
            i += 1
print(numbers(10, 30, 7))

def numbers_2(m, n, k):
    i = n
    while i <= n:
        if i % k == 0:
            return(i)
        else:
            i -= 1
print(numbers_2(10, 30, 7))
        
