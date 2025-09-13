# https://leetcode.com/problems/find-closest-number-to-zero/


class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0]
        get_sign = lambda g: int(abs(g) / g) if g != 0 else 1
        for num in nums:
            if not abs(num) <= abs(closest):
                continue

            if abs(closest) == abs(num) and get_sign(num) < get_sign(closest):
                continue

            closest = num
        return closest
