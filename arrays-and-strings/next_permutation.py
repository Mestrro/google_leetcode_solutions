class Solution(object):
    def reverse(self, nums, counter):
        second_counter = len(nums) - 1
        while (counter < second_counter):
            self.swap(nums, counter, second_counter)
            counter += 1
            second_counter -= 1
        return nums
    def swap(self, nums, counter, second_counter):
        nums[counter], nums[second_counter] = nums[second_counter], nums[counter]
        return nums
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = len(nums) - 2
        while (counter >= 0 and nums[counter + 1] <= nums[counter]):
            counter -= 1
        if (counter >= 0):
            second_counter = len(nums) - 1
            while (nums[second_counter] <= nums[counter]):
                second_counter -= 1
            nums = self.swap(nums, counter, second_counter)
        nums = self.reverse(nums, counter + 1)
        
