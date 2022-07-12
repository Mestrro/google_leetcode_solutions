class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        solutionList = []
        openBrackets = ["(", "[", "{"] 
        for x in s:
            if x in openBrackets:
                solutionList.append(x)
            else:
                if (solutionList == []):
                    return False
                if (x==")"):
                    if (solutionList[-1]=="("):
                        solutionList.pop()
                        continue
                if (x=="]"):
                    if (solutionList[-1]=="["):
                        solutionList.pop()
                        continue
                if (x=="}"):
                    if (solutionList[-1]=="{"):
                        solutionList.pop()
                        continue
                return False
        if (solutionList == []):
            return True
        else:
            return False
