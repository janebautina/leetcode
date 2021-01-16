from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()
        ans = 0
        covered = 0
        for i, h in enumerate(height):
            while stack and stack[-1][1] <= h:
                i_prev, h_prev = stack.pop()
                ans += (h_prev - covered) * (i - i_prev - 1)
                covered = h_prev

            if not stack:
                stack.append((i, h))
                covered = 0
            else:
                i_prev, h_prev = stack[-1]
                ans += (h - covered) * (i - i_prev - 1)
                covered = h
                stack.append((i, h))
        return ans
