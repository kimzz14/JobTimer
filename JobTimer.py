import time, math

class JobTimer:
    def __init__(self):
        self.tic = None

    def reset(self):
        self.tic = time.time()

    def check(self):
        self.toc = time.time()

    def remainTime(self, percentage):
        remainTime = (self.toc - self.tic)/percentage*(1.0-percentage)

        day = math.floor(remainTime/60/60/24)
        hour = math.floor((remainTime - day*60*60*24)/60/60)
        minute = math.floor((remainTime - day*60*60*24 - hour*60*60)/60)
        second = math.floor((remainTime - day*60*60*24 - hour*60*60 - minute*60))

        timeText = str(day).rjust(3, ' ') + ' days, ' + str(hour).rjust(2,'0') + ':' + str(minute).rjust(2,'0') + ':' + str(second).rjust(2,'0')

        return timeText
