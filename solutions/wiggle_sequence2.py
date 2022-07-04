# 376. Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/
 
class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        count = 0
        direct = 0

        for i in range(0, len(nums) - 1):
            if direct == 0:
                if nums[i] > nums[i + 1]:
                    direct = -1
                    count = count + 1
                if nums[i] < nums[i + 1]:
                    direct = 1
                    count = count + 1

            if direct == 1:
                if nums[i] > nums[i + 1]:
                    count = count + 1
                    direct = -1

            if direct == -1:
                if nums[i] < nums[i + 1]:
                    count = count + 1
                    direct = 1

        return count + 1


arr = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]


s = Solution()
v = s.wiggleMaxLength(arr)
print(v)