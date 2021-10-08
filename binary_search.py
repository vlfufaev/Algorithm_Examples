#Given an array of integers nums which is sorted in ascending order,
#and an integer target, write a function to search target in nums.
#If target exists, then return its index. Otherwise, return -1.
#


class Solution(object):
    def search(self, nums, target):
        
        left, right = 0, len(nums)-1

        while left <= right:

            if right == left + 1:# Endpoint 1 || len(nums) == 2
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right  
                else:
                    return -1

            curr = (left + right)//2# General process                 
            if nums[curr] == target:
                return curr
            if nums[curr] > target:
                right = curr - 1
            if nums[curr] < target:
                left = curr + 1

        return -1

S = Solution()
print(Solution.search(S, [1, 2, 3, 4], 5))
