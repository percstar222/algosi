n, m, mod = map(int, input().split())  # Читаем степень, количество x и модуль
coeffs = [int(input()) for _ in range(n + 1)]  # Читаем коэффициенты
x_values = [int(input()) for _ in range(m)]  # Читаем значения x

for x in x_values:  # Для каждого x
    result = 0  # Инициализируем результат
    # Проходим коэффициенты от старшего к младшему (схема Горнера)
    for coeff in reversed(coeffs):
        result = (result * x + coeff) % mod  # Вычисляем значение по модулю
    print(result)  # Выводим результат