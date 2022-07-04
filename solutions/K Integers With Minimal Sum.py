# https://leetcode.com/problems/append-k-integers-with-minimal-sum/


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        hits = {}

        for i in nums:
            if not i in hits:
                hits[i] = 1

        uniq = hits.keys()

        new_int = []
        count = 0
        cur_int = 1
        while (count < k):
            if not cur_int in hits:
                new_int.append(cur_int)
                count = count + 1

            cur_int = cur_int + 1

        sum_arr = 0
        for i in uniq:
            sum_arr = sum_arr + i

        sum_int = 0
        for i in new_int:
            sum_int = sum_int + i

        return min(sum_int, sum_arr + sum_int)

