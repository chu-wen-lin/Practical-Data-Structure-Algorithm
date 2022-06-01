from typing import List
import math
import functools


class Airport:
    def airport(self, houses: List[List[int]]) -> float:
        """
        Find the best place to build airport and
        calculate the average distance from all the house to airport

        Parameters:
            houses(list[list[int]]): List of houses.
                Each house contains [x,y] coordination.

        Returns:
            distance(float)
        """

        self.houses = houses
        self.houses.sort(key=lambda x: (x[1], x[0]))
        self.pivot_x = self.houses[0][0]
        self.pivot_y = self.houses[0][1]

        return self.avg_distance()

    def polar_angle(self, p: List[int]) -> float:
        y_span = p[1] - self.pivot_y
        x_span = p[0] - self.pivot_x
        return math.atan2(y_span, x_span)  # 弧度

    def distance(self, p: List[int]) -> float:
        y_span = p[1] - self.pivot_y
        x_span = p[0] - self.pivot_x
        return math.sqrt(y_span ** 2 + x_span ** 2)

    def key(self, p0: List[int], p1: List[int]) -> int:
        if (self.polar_angle(p0)) == (self.polar_angle(p1)) and (self.distance(p0)) == (self.distance(p1)):
            return 0
        if (self.polar_angle(p0)) == (self.polar_angle(p1)):
            return 1 if (self.distance(p0)) > (self.distance(p1)) else -1
        return 1 if (self.polar_angle(p0)) > (self.polar_angle(p1)) else -1

    def ccw_sort(self) -> List[List[int]]:
        self.houses.sort(key=functools.cmp_to_key(self.key))
        return self.houses

    def det(self, p0: List[int], p1: List[int], p2: List[int]) -> float:
        return ((p1[0] - p0[0]) * (p2[1] - p0[1])) - ((p1[1] - p0[1]) * (p2[0] - p0[0]))
        # >0 :counterclockwise; <0:clockwise; =0:collinear

    def graham_scan(self) -> List[List[int]]:
        convex_hull = []

        for p in self.ccw_sort():
            while len(convex_hull) >= 2 and self.det(convex_hull[-2], convex_hull[-1], p) <= 0:
                a = convex_hull.pop()
            convex_hull.append(p)
        return convex_hull

    def centroid(self):

        x_coords = [p[0] for p in self.ccw_sort()]
        y_coords = [p[1] for p in self.ccw_sort()]
        _len = len(self.houses)
        self.centroid_x = sum(x_coords) / _len
        self.centroid_y = sum(y_coords) / _len

        return [self.centroid_x, self.centroid_y]

    def avg_distance(self) -> float:

        avg_distance = []

        ch = self.graham_scan()
        pivot = ch[0]
        ch.append(pivot)
        # print(ch)
        ct = self.centroid()
        # print(ct)

        for i in range(len(ch) - 1):
            p0_x = ch[i][0]
            p0_y = ch[i][1]
            p1_x = ch[i + 1][0]
            p1_y = ch[i + 1][1]

            lx = p1_x - p0_x
            ly = p1_y - p0_y
            # print("lx=", lx, "ly=", ly)

            distance = abs((ct[0] * ly) - (ct[1] * lx)) / math.sqrt(lx ** 2 + ly ** 2)
            # print("distance=", distance)
            avg_distance.append(distance)

        # print(avg_distance)
        min_distance = min(avg_distance)

        return min_distance
