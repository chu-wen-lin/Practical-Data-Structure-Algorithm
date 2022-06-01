from typing import List
import heapq


class Cluster:
    def cluster(self, points: List[List[int]], cluster_num: int) -> List[List[float]]:
        """
        Cluster the points to cluster_num clusters.
        Output the sorted center coordination of those clusters.
        """
        points = [tuple(ele) for ele in points]
        N = len(points)
        size = {coord: 1 for coord in points}
        h = []

        for i in range(N - 1):
            for j in range(i + 1, N):
                x_dis = (points[i][0] - points[j][0]) ** 2
                y_dis = (points[i][1] - points[j][1]) ** 2
                d = x_dis + y_dis
                h.append((d, points[i], points[j]))

        heapq.heapify(h)

        while N > cluster_num:

            _, p1, p2 = heapq.heappop(h)

            if (p1 not in points) or (p2 not in points):
                continue

            centroid_x = (p1[0] * size[p1] + p2[0] * size[p2]) / (size[p1] + size[p2])
            centroid_y = (p1[1] * size[p1] + p2[1] * size[p2]) / (size[p1] + size[p2])

            size[(centroid_x, centroid_y)] = size[p1] + size[p2]

            points.append((centroid_x, centroid_y))

            points.remove(p1)
            points.remove(p2)

            N -= 1
            for k in range(len(points) - 1):
                x_dis = (points[k][0] - centroid_x) ** 2
                y_dis = (points[k][1] - centroid_y) ** 2
                d = x_dis + y_dis
                heapq.heappush(h, (d, points[k], (centroid_x, centroid_y)))

        points = [list(ele) for ele in points]

        return sorted(points, key=lambda x: (x[0], x[1]))
