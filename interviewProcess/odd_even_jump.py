class Solution(object):
    def get_jumps(self, indexes):
        next_jump = [None] * len(indexes)
        stack = []

        for i in indexes:
            while stack and stack[-1] < i:
                next_jump[stack.pop()] = i
            stack.append(i)

        return next_jump
    
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        idx_sorted = sorted(range(length), key=lambda i: arr[i])
        next_odd_jumps = self.get_jumps(idx_sorted)
        idx_sorted.sort(key=lambda i: -arr[i])
        next_even_jumps = self.get_jumps(idx_sorted)

        odd, even = [False] * length, [False] * length
        odd[-1], even[-1] = True, True
        for i in reversed(range(length - 1)):
            next_odd_jump, next_even_jump = next_odd_jumps[i], next_even_jumps[i]
            if next_odd_jump: odd[i] = even[next_odd_jump]
            if next_even_jump: even[i] = odd[next_even_jump]

        return sum(odd)
