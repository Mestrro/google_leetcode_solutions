class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        length = len(num1) + len(num2)
        answer = [0] * length
        nums = []
        for i in range(0, len(num1)):
            tens = 0
            for j in range(0, len(num2) + 1):
                if (j == len(num2)):
                    answer[i + j] += tens
                    continue
                current = int(num1[i]) * int(num2[j])
                current += tens
                tens = int(current / 10) 
                ones = current % 10
                current_answer_digit = answer[i + j] + ones
                answer[i + j] = (current_answer_digit) % 10
                tens += int(current_answer_digit / 10)
        answer = answer[::-1]
        solution = ""
        print(answer)
        for i in range(0, len(answer)):
            if (i == 0 and answer[i] == 0):
                continue
            solution += str(answer[i])
        return solution
            
            
        
        
