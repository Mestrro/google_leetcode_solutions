class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxi = 0
        while (left < right):
            width = right - left
            space = width * min(height[right], height[left])
            if (space > maxi):
                maxi = space
            if (height[right] < height[left]):
                right -= 1
            else:
                left += 1
        return maxi
