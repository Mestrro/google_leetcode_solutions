class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        solution_set = set()
        for i in range(0, len(emails)):
            counter = 0
            plus = False
            whole_email = ""
            while (counter < len(emails[i])):
                if (plus and emails[i][counter] != "@"):
                    counter += 1
                    continue
                if (emails[i][counter] == "@"):
                    whole_email = whole_email + emails[i][counter:len(emails[i])] 
                    break
                if (emails[i][counter] == "+"):
                    plus = True
                    continue
                if (emails[i][counter] == "."):
                    counter += 1
                    continue
                whole_email = whole_email + emails[i][counter]
                counter += 1
            solution_set.add(whole_email)
        return (len(solution_set))
