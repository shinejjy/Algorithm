import heapq
import math


class Node:
    def __init__(self, fr, nodes=[]):
        self.fr = fr
        self.code = ''
        self.nodes = nodes

    def __lt__(self, other):
        return self.fr < other.fr


n = int(input())
frs = list(map(int, input().split()))
init_node = [Node(fr) for fr in frs]
nodes = [Node(frs[i], [init_node[i]]) for i in range(n)]
heap = []
for node in nodes:
    heapq.heappush(heap, node)
while len(heap) > 1:
    left = heapq.heappop(heap)
    for node in left.nodes:
        node.code = '0' + node.code
    right = heapq.heappop(heap)
    for node in right.nodes:
        node.code = '1' + node.code
    new_code = Node(left.fr + right.fr, left.nodes + right.nodes)
    heapq.heappush(heap, new_code)

for i in range(n):
    print('{} {}'.format(chr(i + 97), init_node[i].code))

compressed = sum([len(init_node[i].code) for i in range(n)])
ori = n * math.ceil(math.log2(n))
print(ori / compressed)
