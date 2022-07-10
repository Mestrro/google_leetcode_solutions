class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0 or len(s) == 1):
            return len(s)
        
        right = 1
        window = s[0]
        maxi = 0
        
        while (right < len(s)):
            if (s[right] in window):
                if (len(window) > maxi):
                    maxi = len(window)
                window = window[window.index(s[right]) + 1 : len(window)]
                window += s[right]
            else:
                window += s[right]
            right += 1
            if (right == len(s)):
                if (len(window) > maxi):
                    maxi = len(window)
                    
        return maxi
