class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        new_time = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]
        mini = 10
        solved = False
        for i in range(0, 3):
            if (new_time[i] > new_time[3]):
                if (new_time[i] - new_time[3] < mini):
                    mini = new_time[i] - new_time[3]
                    solved = True
        if (solved):
            return str(new_time[0]) + str(new_time[1]) + ":" + str(new_time[2]) + str(new_time[3] + mini)
        mini = 10
        for i in range(0, 4):
            if (new_time[i] > new_time[2]):
                if (i == 2):
                    continue
                if (new_time[i] - new_time[2] < mini and new_time[i] < 6):
                    mini = new_time[i] - new_time[2]
                    solved = True
        if (solved):
            return str(new_time[0]) + str(new_time[1]) + ":" + str(new_time[2] + mini) + str(min(new_time)) 
        mini = 10
        for i in range(0, 4):
            if (i == 1):
                continue
            if (new_time[i] > new_time[1]):
                if (new_time[0] < 2):
                    if (new_time[i] - new_time[1] < mini):
                        mini = new_time[i] - new_time[1]
                        solved = True
                if (new_time[0] == 2):
                    if (new_time[i] - new_time[1] < mini and new_time[i] < 4):
                        mini = new_time[i] - new_time[1]
                        solved = True
        if (solved):
            return str(new_time[0]) + str(new_time[1] + mini) + ":" + str(min(new_time)) + str(min(new_time)) 
        for i in range(1, 4):
            if (new_time[i] > new_time[0] and new_time[i] < 3 and new_time[i] - new_time[0] < mini):
                mini = new_time[i] - new_time[0]
                solved = True
        if (solved):
            return str(new_time[0] + mini) + str(min(new_time)) + ":" + str(min(new_time)) + str(min(new_time)) 
        return str(min(new_time)) + str(min(new_time)) + ":" + str(min(new_time)) + str(min(new_time)) 
