class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        starting_point = 0
        new_starting_point = 0
        climber = 0
        checker = set()
        maxi = 0
        while (climber < len(s)):
            if (s[climber] not in checker and len(checker) == 2):
                if (maxi < climber - starting_point):
                    maxi = climber - starting_point
                checker = set()
                checker.add(s[new_starting_point])
                checker.add(s[climber])
                starting_point = new_starting_point
                new_starting_point = climber
            if (s[climber] not in checker and len(checker) < 2):
                new_starting_point = climber
                checker.add(s[climber])
            if (s[climber] in checker and len(checker) == 2 and s[climber] != s[climber - 1]):
                new_starting_point = climber
            climber += 1
            if (climber == len(s)):
                if (maxi < climber - starting_point):
                    maxi = climber - starting_point
        return maxi
