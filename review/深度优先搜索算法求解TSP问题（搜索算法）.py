import copy
from queue import LifoQueue


class Step:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost

    def display(self):
        print('->'.join(list(map(str, self.state))))


n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
q = LifoQueue()
count = 20

best_cost = float('inf')
best_state = None

q.put(Step([1], 0))
while not q.empty():
    step = q.get()
    state, cost = step.state, step.cost
    if cost >= best_cost:
        continue
    if count > 0:
        step.display()
        count = count - 1

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

print("{}: {}".format(best_cost, '->'.join(list(map(str, best_state)))))




