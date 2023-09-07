import queue
import copy

target = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
x, y = list(map(int, input().split()))
plaza = [list(map(int, input().split())) for _ in range(3)]
hole_xy = None
target[x][y] = -1
for i, row in enumerate(plaza):
    for j, val in enumerate(row):
        if val == -1:
            hole_xy = (i, j)
            break

posx = [1, -1, 0, 0]
posy = [0, 0, 1, -1]


class Chess:
    def __init__(self, state, cost, hole):
        self.state = state
        self.cost = cost
        self.hole = hole

    def __lt__(self, other):
        return self.cost < other.cost


S = queue.PriorityQueue()
S.put(Chess(plaza, 0, hole_xy))
best_cost = 0x3f3f3f3f
vis = set()

while not S.empty():
    chess = S.get()
    cost = chess.cost
    plaza = chess.state
    hole = chess.hole

    if cost > best_cost:
        continue

    vis.add(tuple(map(tuple, plaza)))

    f = True
    for i in range(3):
        for j in range(3):
            f = f and (plaza[i][j] == target[i][j])

    if f:
        best_cost = min(best_cost, cost)

    for dx, dy in zip(posx, posy):
        hole_x_new = hole[0] + dx
        hole_y_new = hole[1] + dy
        if 0 <= hole_x_new < 3 and 0 <= hole_y_new < 3:
            plaza_new = copy.deepcopy(plaza)
            temp = plaza_new[hole[0]][hole[1]]
            plaza_new[hole[0]][hole[1]] = plaza_new[hole_x_new][hole_y_new]
            plaza_new[hole_x_new][hole_y_new] = temp
            cost_new = cost + 1
            if tuple(map(tuple, plaza_new)) not in vis:
                S.put(Chess(plaza_new, cost_new, (hole_x_new, hole_y_new)))

print(best_cost)
