from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()

        result = []

        for i, value_a in enumerate(nums[:-2]):
            # correction: no need to check the last number, cuz there is no j to run with

            s = {}  # a dict to store all possible additive inverse: -(value_a+value_b)

            for value_b in nums[i + 1:]:
                if value_b not in s:
                    s[-(value_a + value_b)] = 1
                else:  # value_b in s means it can be offset to 0 by another two elements in nums
                    solution = [value_a, -(value_a + value_b), value_b]
                    result.append(solution)

        return result

