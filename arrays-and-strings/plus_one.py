class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        tens = 0
        for i in range(0, len(digits) + 1):
            print(digits)
            if (i == len(digits)):
                digits.append(1)
                break
            tens = int((digits[i] + 1) / 10)
            digits[i] = (digits[i] + 1) % 10
            if (not tens):
                break
        digits.reverse()
        return digits
