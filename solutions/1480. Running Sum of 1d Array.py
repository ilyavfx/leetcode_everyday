# 1480. Running Sum of 1d Array
 # https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_arr = []
        summ = 0

        for i in nums:
            summ = summ + i
            new_arr.append(summ)

        return new_arr

