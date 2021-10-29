#Given an integer array nums sorted in non-decreasing order,
#return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        result = []
        c1 = 0
        c2 = len(nums)-1
        if c1 == c2:
            return [nums[0]**2]
        while c1 <= c2:
            if nums[c1]**2 >= nums [c2]**2:
                result.append(nums[c1]**2)
                c1 += 1
            elif nums[c1]**2 < nums [c2]**2:
                result.append(nums[c2]**2)
                c2 -= 1
        result = result[::-1]
        return result

SSS = Solution
print(SSS.sortedSquares(SSS, nums = [-5,-3,-2,-1]))
