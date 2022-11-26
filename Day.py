class day():
    def __init__(self):
        self.day = 1

    def nextday(self):
        self.day += 1

    def daypercent(self):
        self.percent = str(self.day/40*100)+"%"

        return self.percent

    def showday(self):

        return ("Day %d" %self.day)








