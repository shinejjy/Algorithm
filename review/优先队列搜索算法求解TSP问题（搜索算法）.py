import copy
from queue import PriorityQueue


class Step:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost

    def get(self):
        return self.state, self.cost

    def display(self):
        return '->'.join(list(map(str, self.state)))

    def __lt__(self, other):
        return self.cost < other.cost


n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

q = PriorityQueue()
q.put(Step([1], 0))

best_cost = 0x3f3f3f
best_state = None

while not q.empty():
    step = q.get()
    state, cost = step.get()

    if cost > best_cost:
        continue

    if len(state) == n and cost + A[0][state[-1] - 1] < best_cost:
        best_cost = cost + A[0][state[-1] - 1]
        best_state = copy.deepcopy(state)
        continue

    for i in range(n, 0, -1):
        if i not in state:
            new_cost = cost + A[i - 1][state[-1] - 1]
            if new_cost < best_cost:
                new_state = copy.deepcopy(state)
                new_state.append(i)
                q.put(Step(new_state, new_cost))

print('{}: {}'.format(best_cost, '->'.join(list(map(str, best_state)))))


