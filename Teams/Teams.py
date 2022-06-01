from typing import List
import sys

x = 1000000
sys.setrecursionlimit(x)


class Teams:
    def teams(self, idols: int, teetee: List[List[int]]) -> bool:

        queue = []
        colors = [None] * idols  # 0:red team, 1:blue team

        # derive a dict of neighbor (key:vertex, value:[vertex's neighbor])
        neighbor = {n: [] for n in range(idols)}
        for i in teetee:
            neighbor[i[0]].append(i[1])
            neighbor[i[1]].append(i[0])

        for vertex in range(idols):
            if colors[vertex] == 0 or colors[vertex] == 1:  # vertex is colored
                continue

            queue.append(vertex)  # enqueue
            colors[vertex] = 0  # color the vertex to be red

            while queue:
                current = queue.pop(0)  # dequeue

                for n in neighbor[current]:
                    if colors[n] == colors[current]:  # n(current's neighbor) is same color as current
                        return False
                    elif colors[n] is None:
                        if colors[current] == 0:
                            colors[n] = 1
                        else:
                            colors[n] = 0

                        queue.append(n)

        return True  # all vertices can be colored iff can be divided into 2 teams
