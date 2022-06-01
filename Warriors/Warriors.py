from typing import List


class Warriors:
    def warriors(self, strength: List[int], attack_range: List[int]):
        """
        Given the attributes of each warriors and output the minimal and maximum
        index of warrior can be attacked by each warrior.

        Parameters:
          strength (List[int]): The strength value of N warriors
          attack_range (List[int]): The range value of N warriors

        Returns:
          attack_interval (List[int]):
              The min and the max index that the warrior can attack.
              The format of output is 2N int array `[a0, b0, a1, b1, ...]`
        """
        # self.d = {}
        N = len(strength)
        stack_l = []  # 左邊的stack
        stack_r = []  # 右邊的stack
        left = [0] * N  # 裝左邊可攻擊對象最後解
        right = [(N - 1)] * N  # 裝右邊可攻擊對象最後解
        output = [None] * (N * 2)

        for i, item in enumerate(strength):
            if not stack_r:
                stack_r.append(i)
                continue

            while stack_r and item >= strength[stack_r[-1]]:
                loser = stack_r.pop(-1)
                right[loser] = i - 1

            stack_r.append(i)  # 小於等於:只會做這件事，把自己的index裝進stack

        for j in range(N - 1, -1, -1):
            if not stack_l:
                stack_l.append(j)
                continue

            while stack_l and strength[j] >= strength[stack_l[-1]]:
                loserr = stack_l.pop(-1)
                left[loserr] = j + 1

            stack_l.append(j)

        for x in range(len(left)):
            diff_l = x - left[x]
            a = min(diff_l, attack_range[x])
            left[x] = x - a

        for y in range(len(right)):
            diff_r = right[y] - y
            b = min(diff_r, attack_range[y])
            right[y] = y + b

        output[::2] = left
        output[1::2] = right

        return output
