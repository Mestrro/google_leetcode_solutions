class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) == 1):
            return True
        
        zeros = [i for i, x in enumerate(nums) if x == 0]
        if (len(zeros) == 0):
            return True
        for i in range(0, len(zeros)):
            lower_bound = -1
            success = False
            for j in range(zeros[i] - 1, lower_bound, -1):
                if (nums[j] > zeros[i] - j or nums[j] + j >= len(nums) - 1):
                    success = True
                    break
            if (success):
                continue
            else:
                return False
        return success
