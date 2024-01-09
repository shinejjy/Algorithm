import heapq


class Node:
    def __init__(self, seq, char=None, left=None, right=None):
        self.seq = seq
        self.pre = None
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.seq < other.seq


def buildHuffmanTree(node_array):
    heap = []
    for node in node_array:
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(seq=left.seq + right.seq, left=left, right=right)
        heapq.heappush(heap, new_node)

    return heap[0]


def traceHuffmanTree(root, code, code_dic):
    if root.left is None and root.right is None:
        code_dic[root.char] = code
    if root.left:
        traceHuffmanTree(root.left, code + '0', code_dic)
    if root.right:
        traceHuffmanTree(root.right, code + '1', code_dic)


n = int(input())
seqs = list(map(int, input().split()))
node_array = [Node(seq, chr(i + 97)) for i, seq in enumerate(seqs)]

root = buildHuffmanTree(node_array)
code_dic = {}
traceHuffmanTree(root, '', code_dic)
for i in range(n):
    char = chr(i + 97)
    print("{} {}".format(char, code_dic[char]))

"""
6
45 13 12 16 9 5
"""
