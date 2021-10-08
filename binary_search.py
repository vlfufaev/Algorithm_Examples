#Given an array of integers nums which is sorted in ascending order,
#and an integer target, write a function to search target in nums.
#If target exists, then return its index. Otherwise, return -1.
#


class Solution(object):
    def search(self, nums, target):            
        left = 0
        right = len(nums)-1
        while left <= right:
            if right == left + 1:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right  
                else:
                    return -1
            curr = (left + right)//2
            if left == curr:
                if nums[curr] == target:
                    return curr
                if nums[curr] != target:
                    return -1
            if nums[curr] == target:
                return curr
            if nums[curr] > target:
                right = curr
            if nums[curr] < target:
                left = curr

S = Solution()
print(Solution.search(S, [1, 2, 4], 4))
