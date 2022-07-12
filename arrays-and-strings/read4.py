# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.queue = deque()
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        done = 0
        amount_left = n
        while (amount_left > 0):
            quad_string = [""] * 4
            read4(quad_string)
            for i in range(0, len(quad_string)):
                self.queue.append(quad_string[i])
            if (len(self.queue) == 0):
                break
            while (amount_left > 0 and len(self.queue) > 0):
                buf[done] = self.queue.popleft()
                done += 1
                amount_left -= 1
        return done
        
