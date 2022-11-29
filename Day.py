class day():
    def __init__(self):
        self.date = 1

    def nextday(self):
        a = True
        if a == True:
            self.date = self.date + 1
            return ("Day %d" %self.date)

    def daypercent(self, day):
        self.percent = day/40*100
        return self.percent






