class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first = len(s) - 1
        second = len(t) - 1
        while (first > -1 or second > -1):
            first_skip = 0
            second_skip = 0
            while (s[first] == "#" and first > -1):
                first -= 1
                first_skip += 1
            while (t[second] == "#" and second > -1):
                second -= 1
                second_skip += 1
            while (first_skip > 0 and first > -1):
                first -= 1
                if (s[first] == "#"):
                    first_skip += 1
                    continue
                else:
                    first_skip -= 1
            while (second_skip > 0 and second > -1):
                second -= 1
                if (t[second] == "#"):
                    second_skip += 1
                    continue
                else:
                    second_skip -= 1
            if (first < 0 and second >= 0 or first >= 0 and second < 0):
                return False
            if (first > -1 and second > -1):
                if (s[first] == t[second]):
                    first -= 1
                    second -= 1
                    continue
                else:
                    return False
        return True
                
                
