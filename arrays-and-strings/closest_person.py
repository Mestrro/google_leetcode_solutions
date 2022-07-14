class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxi = 0
        start = -1
        for i in range(0, len(seats)):
            if (seats[i] == 1):
                if (start == -1):
                    maxi = i
                    start = i
                else:
                    maxi = max(maxi, (i-start)/2) 
                    start = i
            elif (i == len(seats) - 1):
                maxi = max(maxi, (i-start))
        return maxi
