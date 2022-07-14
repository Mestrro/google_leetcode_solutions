class Solution(object):
    def checkIfExpressive(self, expressive, word):
        counter = 0
        second_counter = 0
        char_length = 1
        second_char_length = 1
        if (len(expressive) < len(word)):
            return False
        while (counter < len(word)):
            if (word[counter] != expressive[second_counter]):
                return False
            if (counter < len(word) - 1 and second_counter < len(expressive) - 1 ):
                if (word[counter + 1] == word[counter] and expressive[second_counter + 1] == expressive[second_counter]):
                    counter += 1
                    second_counter += 1
                    char_length += 1
                    second_char_length += 1
                    continue
            while (second_counter < len(expressive) - 1 and expressive[second_counter + 1] == expressive[second_counter]):
                second_char_length += 1
                second_counter += 1
            
            if (second_char_length != char_length and second_char_length < 3):
                return False
            if (counter == len(word) - 1 and second_counter < len(expressive) - 1 and expressive[second_counter] != expressive[second_counter + 1]):
                return False
            second_char_length = 1
            char_length = 1
            counter += 1
            second_counter += 1
            if (second_counter == len(expressive) and counter < len(word)):
                return False
        return True
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        counter = 0
        for i in range(0, len(words)):
            if (self.checkIfExpressive(s, words[i])):
                counter += 1
        return counter
