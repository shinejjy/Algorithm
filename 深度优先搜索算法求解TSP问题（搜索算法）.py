import queue

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]

S = queue.LifoQueue()


class Step:
    def __init__(self, cost, steps):
        self.cost = cost
        self.steps = steps

    def print_step(self):
        print('->'.join(map(str, self.steps)))


best_cost = 0x3f3f3f3f
best_step = None
count = 20
S.put(Step(0, [1]))
while not S.empty():
    step = S.get()

    if step.cost > best_cost:
        continue

    for city in range(n, 0, -1):
        now_cost = step.cost + G[step.steps[-1]-1][city-1]
        if city not in step.steps and now_cost < best_cost:
            now_steps = step.steps.copy()
            now_steps.append(city)
            S.put(Step(now_cost, now_steps))

    if len(step.steps) == n:
        now_cost = step.cost + G[step.steps[-1]-1][0]
        if now_cost < best_cost:
            best_cost = now_cost
            best_step = step

    if count:
        step.print_step()
        count = count - 1

print('{}: '.format(best_cost), end='')
best_step.print_step()
