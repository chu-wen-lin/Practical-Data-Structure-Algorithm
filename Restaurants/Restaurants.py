import functools
import bisect
from typing import List


class Restaurant(object):
    def __init__(self, id: int, rate: int, price: int, distance: int):
        self.id = id
        self.rate = rate
        self.price = price
        self.distance = distance

    def info(self) -> List[int]:
        return [self.id, self.rate, self.price, self.distance]

    def getID(self) -> int:
        return self.id

    def __lt__(self, b) -> bool:
        """
        The natural comparator of Restaurant

        The comparator should compare the restaurants by the value calculated from the formula
        `distance * price / rate`
        and return True if the value of `self` is lower than `b`
        If the value is the same, keep the same order as input.
        """

        va = self.distance * self.price / self.rate
        vb = b.distance * b.price / b.rate

        return va < vb

    @staticmethod
    def comparator1(a, b) -> int:
        """
        Compare two restaurants by restaurant object

        Order the restaurants by the rate in increasing order,
        distance in increasing order (if tied),and
        id in decreasing order (if tied again).

        Parameters:
            a(Restaurant): The restaurant object
            b(Restaurant): The restaurant object

        Return:
            result(int): -1 for restaurant a has smaller order, 1 for restaurant b has smaller order, 0 for equal.
        """

        if a.rate == b.rate and a.distance == b.distance and a.id == b.id:
            return 0

        if a.rate == b.rate and a.distance == b.distance:
            return -1 if a.id > b.id else 1

        if a.rate == b.rate:
            return -1 if a.distance < b.distance else 1

        return -1 if a.rate < b.rate else 1


class Restaurants(object):
    def __init__(self, restaurants: List[Restaurant]):
        self.r_dict = {}  # key表示群組中餐廳評分
        self.price_dict = {}

        r_list = [rest.info() for rest in restaurants]

        for ii in range(1, 6):
            self.r_dict[ii] = [rest for rest in r_list if rest[1] == ii]
            self.r_dict[ii].sort(key=lambda x: x[2])
            self.price_dict[ii] = [rest[2] for rest in self.r_dict[ii]]

    def filter(self, min_price: int, max_price: int, min_rate: int) -> List[int]:
        """
        Filter the restaurants, output the list of restaurant id that meet the condition.

        Output the list in in the increasing order of distance;
        If the distance is the same, order the restaurant ids from the highest to the lowest.

        Return:
            restaurants (List[int]): The list of restaurant id.
        """

        ans = []
        for ii in range(min_rate, 6):
            price_list = self.price_dict[ii]
            pos_lower = bisect.bisect_left(price_list, min_price)
            pos_upper = bisect.bisect_right(price_list, max_price)
            ans += self.r_dict[ii][pos_lower: pos_upper]

        ans.sort(key=lambda x: (x[3], -x[0]))
        return [i[0] for i in ans]
