from itertools import combinations

n, k, m = map(int, input().split())  # Читаем параметры задачи
graph = {i: set() for i in range(1, n+1)}  # Создаем граф знакомств
for _ in range(m):  # Читаем пары знакомых
    u, v = map(int, input().split())
    graph[u].add(v)  # Добавляем в граф
    graph[v].add(u)  # Обе связи (граф неориентированный)

max_cohesion = -1  # Максимальная сплоченность
best_team = None  # Лучшая команда

# Перебираем все возможные команды размера k
for team in combinations(range(1, n+1), k):
    cohesion = 0  # Счетчик сплоченности для текущей команды
    # Перебираем все пары в команде
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            if team[j] in graph[team[i]]:  # Если знакомы
                cohesion += 1  # Увеличиваем сплоченность
    # Если нашли команду с большей сплоченностью
    if cohesion > max_cohesion:
        max_cohesion = cohesion  # Обновляем максимум
        best_team = team  # Запоминаем лучшую команду

print(' '.join(map(str, best_team)))  # Выводим лучшую команду