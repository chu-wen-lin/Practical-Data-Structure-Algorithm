from typing import List
from heapq import heappop, heappush


class Mountains:
    def mountains(self, mountains_height: List[List[int]]):

        N = len(mountains_height)
        M = len(mountains_height[0])

        queue = [(mountains_height[0][0], 0, 0)]
        cost = {(i, j): float('inf') for i in range(N) for j in range(M)}
        cost[(0, 0)] = 0

        visited = set()
        # directions = [(1,0), (0,1), (-1, 0), (0, -1)]  #down, right, up, left

        while queue:
            height, r, c = heappop(queue)
            visited.add((r, c))

            if (r, c) == (N - 1, M - 1):
                return cost[(N - 1, M - 1)]

            for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= i < N and 0 <= j < M and (i, j) not in visited:
                    if mountains_height[r][c] >= mountains_height[i][j]:
                        edge_cost = mountains_height[r][c] - mountains_height[i][j]
                    else:
                        edge_cost = 2 * (mountains_height[i][j] - mountains_height[r][c])

                    # relaxation
                    if cost[(r, c)] + edge_cost < cost[(i, j)]:
                        cost[(i, j)] = cost[(r, c)] + edge_cost  # update cost
                        heappush(queue, (cost[(i, j)], i, j))  # push into heap
