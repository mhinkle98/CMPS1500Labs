
class MilClock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        if self.hour < 10:
            selfHourString = '0' + str(self.hour)
        if self.minute < 10:
            selfMinuteString = '0' + str(self.minute)
        return selfHourString + ":" + selfMinuteString
        

    def addOne(self):
        if self.minute < 59:
            self.minute += 1
        elif self.minute == 59:
            self.minute = 0
            self.hour += 1
