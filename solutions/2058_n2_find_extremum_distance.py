#2058. Find the Minimum and Maximum Number

#https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def findExtremumDistance(self,values) -> list[int]:
        critical = self.find_critical(values)
        ret = self.meathure_critical(critical)
        return ret

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        values = self.copy_to_list(head)
        critical = self.find_critical(values)
        ret = self.meathure_critical(critical)
        return ret

    def copy_to_list(self, head: Optional[ListNode]):
        values = []
        node = head

        while True:
            values.append(node.val)
            node = node.next
            if node.next == None:
                values.append(node.val)
                break

        return values

    def find_critical(self, values) -> list[int]:
        critical = [0 for x in values]
        for i in range(1, len(values) - 1):
            if (((values[i] > values[i - 1]) and (values[i] > values[i + 1])) or
                    ((values[i] < values[i - 1]) and (values[i] < values[i + 1]))):
                critical[i] = 1

        return critical

    def meathure_critical(self, critical) -> list[int]:
        min_dist = len(critical)
        max_dist = -1
        for i in range(1, len(critical) - 1):
            for j in range(i + 1, len(critical) - 1):
                if critical[i] == 1 and critical[j] == 1:
                    if abs(i - j) < min_dist:
                        min_dist = abs(i - j)
                    if abs(i - j) > max_dist:
                        max_dist = abs(i - j)

        if min_dist == len(critical):
            min_dist = -1

        return [min_dist, max_dist]



s = Solution()
print(s.findExtremumDistance([5,3,1,2,5,1,2]))
