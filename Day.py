class day():
    def nextday(self):
        a = True
        self.day = 1
        if a == True:
            self.day = self.day + 1
            return ("Day %d" %self.day)

    def daypercent(self):
        self.percent = self.day/40*100
        return str(self.percent)+"%"






