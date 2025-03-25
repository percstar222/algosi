n = int(input())  # Читаем количество камней
weights = list(map(int, input().split()))  # Читаем веса камней
total = sum(weights)  # Сумма всех весов
min_diff = float('inf')  # Инициализируем минимальную разницу

# Перебираем все возможные подмножества камней
for mask in range(1 << n):
    sum1 = 0  # Сумма весов в первой куче
    for i in range(n):
        if mask & (1 << i):  # Если камень в подмножестве
            sum1 += weights[i]  # Добавляем его вес
    # Вычисляем разницу весов куч
    diff = abs(total - 2 * sum1)
    if diff < min_diff:  # Если нашли меньшую разницу
        min_diff = diff  # Обновляем минимум

print(min_diff)  # Выводим минимальную разницу