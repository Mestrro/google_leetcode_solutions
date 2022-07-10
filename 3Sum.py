class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        current = 0
        solutions = []
        for i in range(0, len(nums) - 1):
            if (nums[i] > 0):
                break;
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                if (nums[left] + nums[right] + nums[i] > 0):
                    right -= 1
                elif (nums[left] + nums[right] + nums[i] < 0):
                    left += 1
                elif (nums[left] + nums[right] + nums[i] == 0):
                    if [nums[i], nums[left], nums[right]] not in solutions:
                        solutions.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return solutions
