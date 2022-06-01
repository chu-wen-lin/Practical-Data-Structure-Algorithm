class WeightedQuickUnionUF:
    def __init__(self, N):
        self.parent = [ii for ii in range(N)]
        self.sz = [1] * N

    def root(self, p: int):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        """Is this site p(i,j) connected to q ?"""
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        r1 = self.root(p)
        r2 = self.root(q)
        if r1 == r2:
            return
        if self.sz[r1] < self.sz[r2]:
            self.parent[r1] = r2  # 把q的root指給p
            self.sz[r2] += self.sz[r1]
        else:
            self.parent[r2] = r1
            self.sz[r1] += self.sz[r2]


class Percolation:
    def convertIndex(self, i: int, j: int):
        # input row, col index(starting from zero) in the matrix
        # return index of corresponding 1D list

        return i * self.N + j + 1

    def __init__(self, N: int):
        """ Create N-by-N grid, with all sites blocked """
        self.N = N

        self.grid = [False for ii in range(N * N + 2)]  # blocked:0 ; open:1
        self.perc = WeightedQuickUnionUF(N * N + 2)
        self.full = WeightedQuickUnionUF(N * N + 2)

        self.virtual_top = 0
        self.virtual_bottom = N * N + 1

        self.grid[self.virtual_top] = True
        self.grid[self.virtual_bottom] = True

        for jj in range(N):
            ii = 0
            topSiteIndex = self.convertIndex(ii, jj)
            self.perc.union(self.virtual_top, topSiteIndex)
            self.full.union(self.virtual_top, topSiteIndex)

            ii = N - 1
            bottomSiteIndex = self.convertIndex(ii, jj)
            self.perc.union(self.virtual_bottom, bottomSiteIndex)

    def open(self, i: int, j: int):  # row:i  column:j
        """ Open site (row i, column j) if it is not open already """

        siteIndex = self.convertIndex(i, j)

        if not self.isOpen(i, j):
            self.grid[siteIndex] = True

            for loc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                i_new = i + loc[0]
                j_new = j + loc[1]

                if (i_new >= 0) and (j_new >= 0) and (i_new <= self.N - 1) and (j_new <= self.N - 1):
                    neighborSiteIndex = self.convertIndex(i_new, j_new)
                    if self.isOpen(i_new, j_new):
                        self.perc.union(siteIndex, neighborSiteIndex)
                        self.full.union(siteIndex, neighborSiteIndex)

    def isOpen(self, i: int, j: int) -> bool:
        """ Is site (row i, column j) open? """
        siteIndex = self.convertIndex(i, j)

        return self.grid[siteIndex]

    def isFull(self, i: int, j: int) -> bool:
        """ Is site (row i, column j) full?
        We guarantee that site(i,j) is open when we call isFull.
        Note that 0 <= i < N and 0 <= j < N.
        """
        siteIndex = self.convertIndex(i, j)

        if self.N == 1:
            return self.isOpen(0, 0)
        else:
            return self.full.connected(self.virtual_top, siteIndex) and (self.isOpen(i, j))

    def percolates(self) -> bool:
        """ Does the system percolate? """
        if self.N == 1:
            return self.isOpen(0, 0)
        else:
            return self.perc.connected(self.virtual_top, self.virtual_bottom)
