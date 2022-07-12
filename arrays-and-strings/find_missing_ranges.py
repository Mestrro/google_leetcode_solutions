class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        solution = []
        if (len(nums) == 0):
            if (lower == upper):
                solution.append(str(lower))
            else:
                solution.append(str(lower) + "->" + str(upper))
        for i in range(0, len(nums)):
            if (i == 0):
                if (lower < nums[i] and nums[i] - lower > 1):
                    solution.append(str(lower) + "->" + str(nums[i] - 1))
                if (nums[i] - lower == 1):
                    solution.append(str(lower))
            if (i != 0):
                if (nums[i] - nums[i - 1] > 2):
                    solution.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
                if (nums[i] - nums[i - 1] == 2):
                    solution.append(str(nums[i] - 1))
            if (i == (len(nums) - 1)):
                if (upper > nums[i] and upper - nums[i] > 1):
                    solution.append(str(nums[i] + 1) + "->" + str(upper))
                if (upper - nums[i] == 1):
                    solution.append(str(upper))
        return solution            
        
