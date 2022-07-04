#2058. Find the Minimum and Maximum Number

#https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        prev = head
        curr = head.next
        idx = 2
        critical_points = []
        min_dist = float('inf')
        max_dist = -1

        while curr.next:
            if (prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                if (len(critical_points) > 0):
                    min_dist = min(min_dist, idx - critical_points[-1])

                critical_points.append(idx)

            idx += 1

            prev = curr
            curr = curr.next

        if len(critical_points) < 2:
            return [-1, -1]

        max_dist = critical_points[-1] - critical_points[0]

        return [min_dist, max_dist]