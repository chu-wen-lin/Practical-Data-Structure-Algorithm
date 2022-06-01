from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = {}
        result = []

        nums.sort()  # sorting

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                current_sum = nums[i] + nums[j]   # calculate (c+d)
                difference = target - current_sum  # calculate target-(c+d)

                if difference in s:  # means it finds its additive inverse
                    for pair in s[difference]:
                        result.append(pair + [nums[i], nums[j]])  # append the solution:[a,b,c,d] into result

            for k in range(i):
                current_sum = nums[k] + nums[i]
                if current_sum not in s:     # store (a+b) into s as key if it doesn't exist yet
                    s[current_sum] = []
                s[current_sum].append([nums[k], nums[i]])  # store [a,b] into (a+b)'s value:[]

        return result
