class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        reverse = upper(s[::-1].replace('-', ''))
        i = 0
        while i + k < len(reverse):
            reverse = reverse[:(i + k)] + "-" + reverse[(i + k):]
            i += k + 1
        return reverse[::-1]
            
