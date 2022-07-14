class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = s
        res_index = dict()
        for i in range(0, len(indices)):
            if (s[indices[i]:len(sources[i]) + indices[i]] == sources[i]):
                res_helper = 0
                for key in res_index:
                    if (indices[i] > key):
                        res_helper += res_index[key]
                res = res[:indices[i] + res_helper] + targets[i] + res[indices[i] + len(sources[i]) + res_helper:]
                res_index[indices[i]] = len(targets[i]) - len(sources[i]) 
        return res
