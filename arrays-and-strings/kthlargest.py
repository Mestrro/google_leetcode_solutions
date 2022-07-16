import random
class Solution(object):
    def partition(self, pivot, num_list, k):
        new_list = []
        new_list.append(num_list[pivot])
        for i in range(0, len(num_list)):
            if (i == pivot):
                continue
            if (num_list[i] < num_list[pivot]):
                new_list.insert(0, num_list[i])
            else:
                new_list.append(num_list[i])
        return new_list, new_list.index(num_list[pivot])
    def quickSort(self, nums, k):
        pivot = random.randint(0, len(nums) - 1)
        new_list, index_of_pivot = self.partition(pivot, nums, k)
        if (len(nums) == 1):
            return nums[0]
        if (index_of_pivot == k):
            return new_list[index_of_pivot]
        if (index_of_pivot > k):
            return self.quickSort(new_list[0 : index_of_pivot], k)
        else:
            return self.quickSort(new_list[index_of_pivot + 1: len(new_list)], k - index_of_pivot - 1)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums, len(nums) - k)
        
