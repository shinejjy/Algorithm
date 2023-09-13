import queue
import copy


class Step:
    def __init__(self, cost, steps):
        self.cost = cost
        self.steps = steps

    def print_step(self):
        return '->'.join(map(str, self.steps))

    def __lt__(self, other):
        return self.cost < other.cost


q = queue.PriorityQueue()
n = int(input())
G = [list(map(int, input().split(' '))) for _ in range(n)]
best_step = None
best_cost = 0x3f3f3f


q.put(Step(0, [1]))
while not q.empty():
    step = q.get()
    steps = step.steps
    cost = step.cost
    if step.cost >= best_cost:
        continue

    if len(steps) == n and best_cost > cost + G[0][steps[n-1] - 1]:
        best_cost = cost + G[0][steps[-1] - 1]
        best_step = step

    for i in range(1, n+1):
        if i not in step.steps and best_cost > cost + G[i - 1][steps[-1] - 1]:
            now_steps = copy.deepcopy(steps)
            now_steps.append(i)
            now_cost = cost + G[i - 1][steps[-1] - 1]
            q.put(Step(now_cost, now_steps))

print('{}: {}'.format(best_cost, best_step.print_step()))
