class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        solution = 0
        left_max = []
        right_max = [0] * len(height)
        left_max.append(height[0])
        for i in range(1, len(height)):
            left_max.append(max(height[i], left_max[i-1]))
        right_max[len(height) - 1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(0, len(height) - 1):
            solution += min(left_max[i], right_max[i]) - height[i]
        return solution
