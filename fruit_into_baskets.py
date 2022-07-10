class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        new_fruit_index = 0
        maxi = 0
        current_fruits = set()
        current_fruits.add(fruits[left])
        if (len(fruits)==1):
            return 1
        while (right < len(fruits)):
            right += 1
            if (right == len(fruits)):
                if (maxi < (right - left)):
                    maxi = right - left
                break
            if (fruits[right] not in current_fruits and len(current_fruits) < 2):
                current_fruits.add(fruits[right])
            if (fruits[right] in current_fruits and fruits[right] != fruits[new_fruit_index]):
                new_fruit_index = right
            if (fruits[right] not in current_fruits and len(current_fruits) == 2):
                if (maxi < (right - left)):
                    maxi = right - left
                current_fruits = set()
                current_fruits.add(fruits[new_fruit_index])
                left = new_fruit_index
                new_fruit_index = right
                current_fruits.add(fruits[right])
        return maxi
            
