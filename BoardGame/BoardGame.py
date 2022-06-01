from typing import List


class WeightedQuickUnionUF:
    def __init__(self):
        self.parent = {}  # 一開始每顆棋的root都是自己
        self.sz = {}  # 一開始沒有人和別人連在一起，size都是1
        self.peri = {}  # 讓每顆棋子一開始的周長都是0

    def root(self, p: int):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    #     def connected(self, p:int, q:int) -> bool:
    #         """Is this site p(i,j) connected to q ?"""
    #         return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        r1 = self.root(p)
        r2 = self.root(q)
        if r1 == r2:
            return
        if self.sz[r1] < self.sz[r2]:
            self.parent[r1] = r2  # 把q的root(r2)指給p的root(r1)
            self.sz[r2] += self.sz[r1]
            self.peri[r2] += self.peri[r1]
        else:
            self.parent[r2] = r1
            self.sz[r1] += self.sz[r2]
            self.peri[r1] += self.peri[r2]


class BoardGame:
    def __init__(self, h: int, w: int):
        """
        Set the width and height of the board

        Parameters:
            h (int): The height of the board
            w (int): The width of the board
        """
        self.chipan = {}
        self.h = h
        self.w = w
        self.lien = WeightedQuickUnionUF()

    def convertIndex(self, p: tuple) -> int:
        """convert coordinate to index"""
        return (p[1] * self.h) + p[0]  # (0,0):0 (0,1):1 ...

    def putStone(self, x: List[int], y: List[int], stoneType: str):
        """
        Put the stone at (x[i],y[j]) on the board.

        We grantee that there are not stones at (x[i],y[j]) on the board initially.

        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizontal position of the stone, 0 <= y < w
            stoneType (string): The type of the stone to be put on the board, which has only two options {'O', 'X'}
        """

        for i, j in zip(x, y):
            self.chipan[(i, j)] = stoneType

            siteIndex = self.convertIndex((i, j))
            self.lien.parent[siteIndex] = siteIndex
            self.lien.sz[siteIndex] = 1
            self.lien.peri[siteIndex] = 0

            for loc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_loc = tuple(sum(z) for z in zip((i, j), loc))
                neighborSiteIndex = self.convertIndex(new_loc)

                if (0 <= new_loc[0] <= self.h) and (0 <= new_loc[1] <= self.w):  # 沒有超出邊界

                    # 調整周長
                    if new_loc in self.chipan.keys():  # 這顆棋的上/下/左/右：new_loc上，有棋子 --> 自己的周長不動，別人的周長-1

                        self.lien.peri[self.lien.root(neighborSiteIndex)] -= 1

                        # 判斷這顆棋子和上/下/左/右的棋子是否同類 --> 同類的話union；不同類不做事
                        if self.sameStone((i, j), new_loc):
                            self.lien.union(siteIndex, neighborSiteIndex)

                    else:  # 這顆棋的上/下/左/右沒棋子 --> 自己的周長+1

                        self.lien.peri[self.lien.root(siteIndex)] += 1
                else:
                    self.lien.peri[self.lien.root(siteIndex)] += 1

    def sameStone(self, p: tuple, q: tuple) -> bool:
        """Whether p(x1,y1) and q(x2,y2) are of the same stone type ?"""
        return self.chipan[p] == self.chipan[q]

    def surrounded(self, x: int, y: int) -> bool:
        """
        Answer if the stone and its connected stones are surrounded by another type of stones, which means they are qualified to be flipped if we want.

        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizontal position of the stone, 0 <= y < w
        Returns:
            surrounded (bool): can be flipped of not.
        """
        #         if self.h*self.w == 1:
        #             return False

        if (0 < x < self.h) and (0 < y < self.w):  # 在邊界上的點皆為False
            siteIndex = self.convertIndex((x, y))
            return self.lien.peri[self.lien.root(siteIndex)] == 0  # p == 0
        else:
            return False

    def getStoneType(self, x: int, y: int) -> str:
        """
        Get the type of the stone at (x,y)

        We grantee that there are stones at (x,y)

        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizontal position of the stone, 0 <= y < w
        Returns:
            stoneType (string): The type of the stones, which has only two value {'O', 'X'}
        """
        return self.chipan[(x, y)]
