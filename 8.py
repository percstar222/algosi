def is_safe(board, row, col, n):
    """Проверка, можно ли поставить магараджу в (row, col)"""
    # Проверка по горизонтали и вертикали
    for i in range(n):
        if board[row][i] or board[i][col]:
            return False
    # Проверка диагоналей
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False
    # Проверка хода коня
    moves = [(-2,-1),(-1,-2),(1,-2),(2,-1),
             (2,1),(1,2),(-1,2),(-2,1)]
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < n and board[r][c]:
            return False
    return True

def count_placements(n, k, row=0, placed=0):
    """Рекурсивный подсчет расстановок"""
    if placed == k:  # Если расставили всех магарадж
        return 1  # Нашли одну валидную расстановку
    if row == n:  # Если прошли все строки
        return 0  # Не смогли расставить всех
    total = 0
    # Пробуем поставить магараджу в текущей строке
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True  # Ставим магараджу
            total += count_placements(n, k, row+1, placed+1)
            board[row][col] = False  # Убираем магараджу
    # Пробуем не ставить магараджу в текущей строке
    total += count_placements(n, k, row+1, placed)
    return total

n, k = map(int, input().split())  # Читаем размер доски и количество фигур
board = [[False]*n for _ in range(n)]  # Создаем пустую доску
print(count_placements(n, k))  # Выводим количество расстановок