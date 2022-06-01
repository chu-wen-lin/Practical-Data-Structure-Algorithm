from typing import List


class Railway:
    def __init__(self):
        pass

    def railway(self, landmarks: int, distance: List[List[int]]) -> int:

        distance.sort(key=lambda a: a[2])  # sort all edges by weight
        parent = [i for i in range(landmarks + 1)]  # initially, all vertices's parent is themselves

        def find(x):
            # if x == parent[x]:
            #     return parent[x]
            # return find(parent[parent[x]])
            if x != parent[x]:
                parent[x] = find(parent[parent[x]])
            return parent[x]

        sum_distance, e, k = 0, 0, 0
        while e < landmarks - 1:  # number of MST's edges = V-1
            u, v, d = distance[k]  # d:weight(distance)

            k += 1
            x = find(u - 1)
            y = find(v - 1)

            if x != y:
                e += 1
                sum_distance += d
                parent[x] = y

        return sum_distance
