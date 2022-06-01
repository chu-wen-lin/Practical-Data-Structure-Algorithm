from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # build a dict to store index and value
        for index, value in enumerate(nums):
            # (target - value) already in hashmap --> return index & hashmap's "value"
            if target - value in hashmap:
                return [hashmap[target - value], index]
            # (target - value) not in hashmap --> store index and value into hashmap
            else:
                hashmap[value] = index
