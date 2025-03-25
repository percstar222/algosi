def read_set():
    """Функция для чтения множества чисел до нуля"""
    s = set()  # Создаем пустое множество
    while True:
        num = int(input())  # Читаем число
        if num == 0:  # Если встретили 0 - конец ввода
            break
        s.add(num)  # Добавляем число в множество
    return s

A = read_set()  # Читаем первое множество
B = read_set()  # Читаем второе множество
# Находим симметрическую разность и сортируем результат
result = sorted(A.symmetric_difference(B))
# Выводим результат или 0, если множество пустое
print(' '.join(map(str, result)) if result else 0)