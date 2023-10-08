import math
import copy


class Dis:  # Dis类存储一对点距离信息（两个点+距离）
    def __init__(self, point_x, point_y, points_distance):
        self.point_x = point_x
        self.point_y = point_y
        self.distance = points_distance

    def display(self):
        print('{:.1f}'.format(self.distance))
        for data in self.point_x:
            print(data, end=' ')
        print()
        for data in self.point_y:
            print(data, end=' ')
        print()

    def __lt__(self, other):
        return self.distance < other.distance


n = int(input())
points = [list(map(eval, input().split())) for _ in range(n)]
dis = {}

points = sorted(points, key=lambda x: x[0])


def distance(point_x, point_y):
    return math.sqrt((point_x[0] - point_y[0]) ** 2 + (point_x[1] - point_y[1]) ** 2)


def Merge(l, r, m, o):
    if dis[o * 2].distance < dis[o * 2 + 1].distance:
        dis[o] = dis[o * 2]
    else:
        dis[o] = dis[o * 2 + 1]

    # 读取中间段的点对距离
    temp_distance = dis[o].distance
    temp_points = []
    for i in range(l, r + 1):
        if points[m][0] + temp_distance >= points[i][0] >= points[m][0] - temp_distance:
            temp_points.append(copy.deepcopy(points[i]))

    len_temp = len(temp_points)

    dis_temp = []

    for i in range(len_temp - 1):
        for j in range(i + 1, len_temp):
            dis_temp.append(Dis(
                temp_points[i],
                temp_points[j],
                distance(temp_points[i], temp_points[j])
            ))

    if dis_temp:
        dis_temp = sorted(dis_temp)
        if dis[o].distance > dis_temp[0].distance:
            dis[o] = dis_temp[0]


def MergeSort(l, r, o):
    if r == l + 1:  # 两个点时，直接构造Dis
        dis[o] = Dis(
            points[l],
            points[r],
            distance(points[l], points[r]))
        return
    elif r == l:  # 一个点时，构造成inf
        dis[o] = Dis(
            points[l],
            points[r],
            float('inf')
        )
        return

    m = (l + r) // 2
    MergeSort(l, m, o * 2)
    MergeSort(m + 1, r, o * 2 + 1)
    Merge(l, r, m, o)


MergeSort(0, len(points) - 1, 1)
dis[2].display()
dis[3].display()
dis[1].display()
