class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = Counter(t)
        checker = {}
        unique_length = len(counter)
        unique_counter = 0
        left = 0
        right = 0
        solution_coords = 10000000, None, None
        while (right < len(s)):
            if (s[right] not in checker):
                checker[s[right]] = 0
            checker[s[right]] += 1
            if (s[right] in counter and checker[s[right]] == counter[s[right]]):
                unique_counter += 1
            while left <= right and unique_counter == unique_length:
                if (right - left + 1 < solution_coords[0]):
                    solution_coords = (right - left + 1, left, right)
                checker[s[left]] -= 1
                
                if (s[left] in counter and checker[s[left]] < counter[s[left]]):
                    unique_counter -= 1
                left += 1
            right += 1
        if (solution_coords[0] == 10000000):
            return ""
        return s[solution_coords[1] : solution_coords[2] + 1]
