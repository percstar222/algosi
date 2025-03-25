n = int(input())  # Читаем длину улицы
street = list(map(int, input().split()))  # Читаем саму улицу
result = [float('inf')] * n  # Инициализируем массив результатов бесконечностями

# Первый проход слева направо - ищем нули слева
last_zero = -float('inf')  # Позиция последнего нуля слева
for i in range(n):
    if street[i] == 0:
        last_zero = i  # Обновляем позицию последнего нуля
        result[i] = 0  # Для нуля расстояние 0
    else:
        # Расстояние до последнего нуля слева
        result[i] = i - last_zero

# Второй проход справа налево - ищем нули справа
last_zero = float('inf')  # Позиция последнего нуля справа
for i in range(n-1, -1, -1):
    if street[i] == 0:
        last_zero = i  # Обновляем позицию последнего нуля
        result[i] = 0  # Для нуля расстояние 0
    else:
        # Выбираем минимальное расстояние из левого и правого проходов
        result[i] = min(result[i], last_zero - i)

print(' '.join(map(str, result)))  # Выводим результат