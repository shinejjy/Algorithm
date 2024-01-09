"""
02_lcs.py：动态规划法解最长公共子序列问题。

【问题描述】使用动态规划算法解最长公共子序列问题，具体来说就是，依据其递归式自底向上的方式
依次计算得到每个子问题的最优值。
【输入形式】在屏幕上输入两个序列X和Y，序列各元素间都以一个空格分隔。
【输出形式】序列X = {x1, ..., xm}和序列Y = {y1, ..., yn}的最长公共子序列的长度。序列X
和Y的其中一个最长公共子序列，也就是当序列X和Y有多个最长公共子序列时，只输出其中的一个。这
个输出的最长公共子序列选取的方法是：当xi不等于yj时，而c[i-1,j]==c[i,j-1]，那么，c[i,j]
是由c[i-1,j]得到的。其中c[i,j]中存放的是：序列Xi = {x1, ..., xi}和序列Yj = {y1, ..., yj}
的最长公共子序列的长度。
当最长公共子序列为空时，输出最长公共子序列长度为0，最长公共子序列为：None。
【样例1输入】
A B C B D A B
B D C A B A
【样例1输出】
4
BCBA
【样例1说明】
 输入：第一行输入序列X的各元素，第二行输入序列Y的各元素，元素间以空格分隔。
 输出：序列X和Y的最长公共子序列的长度为4，其中一个最长公共子序列为：BCBA。
"""
import numpy as np

def DynamicLcsLength(x, y, m, n):
    """
    动态规划算法解最长公共子序列问题
    输入：
        x - 一维list，x[0]弃用。序列{x1, ..., xm}
        y - 一维list，y[0]弃用。序列{y1, ..., xn}
        m, n - 序列x和y的元素个数
    输出：
        c - nparray, shape(m+1, n+1)。矩阵c中元素c[i,j]中存放的是：序列Xi = {x1, ..., xi}和
            序列Yj = {y1, ..., yj}的最长公共子序列的长度。
        b - nparray, shape(m+1, n+1)。b[i][j]记录c[i, j]的值是由哪一个子问题的解得到的，该值
            在构造最长公共子序列时需要。
            值为1：表示Xi和Yj的最长公共子序列与Xi-1和Yj的最长公共子序列相同
            值为2：表示Xi和Yj的最长公共子序列与Xi和Yj-1的最长公共子序列相同
            值为3：表示Xi和Yj的最长公共子序列与Xi-1和Yj-1的最长公共子序列相同
    """
    # 初始化c和b
    c = np.zeros((m+1, n+1), dtype=np.int8)
    b = np.zeros((m+1, n+1), dtype=np.int8)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i] == y[j]:
                c[i, j] = c[i-1, j-1]+1
                b[i, j] = 3
            elif c[i-1, j] >= c[i, j-1]:
                c[i, j] = c[i - 1, j]
                b[i, j] = 1
            else:
                c[i, j] = c[i, j-1]
                b[i, j] = 2

    return c, b


def PrintLcs(b, x, i, j):
    """
    输出序列Xi = {x1, ..., xi}和序列Yj = {y1, ..., yj}的最长公共子序列
    输入：
        b - nparray, shape(n+1, n+1)。b[i][j]记录c[i, j]的值是由哪一个子问题的解得到的，该值
            在构造最长公共子序列时需要。
        x - 一维list，x[0]弃用。序列{x1, ..., xm}
        i, j - 序列x中最大序号元素为xi; 序列y中最大序号元素为yj
    输出：
        序列Xi和Yj的最长公共子序列
        
    """
    if i == 0 or j == 0:
        return
    if b[i, j] == 3:
        PrintLcs(b, x, i-1, j-1)
        print(x[i], end="")
    elif b[i, j] == 1:
        PrintLcs(b, x, i-1, j)
    else:
        PrintLcs(b, x, i, j-1)


def main():
    # 输入序列X，比如：A B C B D A B
    x = input().split()
    x.insert(0, '0')
    # 输入序列Y，比如：B D C A B A
    y = input().split()
    y.insert(0, '0')

    c, b = DynamicLcsLength(x, y, len(x)-1, len(y)-1)
    # 最长公共子序列的长度
    print(c[-1, -1])
    # print(b[1:, 1:])

    # 输出最长公共子序列
    if c[-1, -1]==0:
        print('None')
    else:
        PrintLcs(b, x, len(x)-1, len(y)-1)


if __name__ == '__main__':
    main()

