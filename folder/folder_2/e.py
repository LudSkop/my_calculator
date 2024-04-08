# Розрахувати прибуток без затрат на матеріали , якщо: р - ціна за 1 листівку, n - це кількість заказаних листівок і може бути тільки кратне 100







def profit(p, n):
    if n %100 != 0:
        print('Введіть число кратне 100: ')
        return
    namber_order = n // 100
    return p * n - namber_order * (75 + 120 + 20)

print(profit(235, 500))
print(profit(189, 800))
print(profit(230, 39))
print(profit(50, 299))







